# Script is originally taken from https://github.com/imartinez/privateGPT/blob/main/privateGPT.py
# and i've added some STT and TTS stuff.

from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.vectorstores import Chroma
from langchain_community.llms import GPT4All, LlamaCpp
import os
import io
import sys
import speech_recognition as sr
from constants import CHROMA_SETTINGS
import pyttsx3
import numpy as np
import argparse
import torch

import whisper
from TTS.api import TTS
import pygame
import time
import keyboard
import chromadb

from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler


from datetime import datetime, timedelta
from queue import Queue
from time import sleep
from sys import platform
import threading


# IMPORT GUI FILE
from src.ui_interface import Ui_MainWindow
##########################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
########################################################################

load_dotenv()
pygame.mixer.init()
##############################
# Whisper for local STT part #
##############################


def record_audio():
    global text
    print("Currently recording")

    # Load the speech recognizer and set the initial energy threshold and pause threshold
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.pause_threshold = 0.8
    r.dynamic_energy_threshold = False

    with sr.Microphone(sample_rate=16000) as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise before recording

        # Initialize variables
        i = 0
        silence_counter = 0
        max_silence_threshold = 3  # Maximum consecutive seconds of silence before stopping recording

        # Start recording loop
        # while True:
        # Listen to the user's voice
        audio = r.listen(source)

        # Convert audio to torch tensor
        torch_audio = torch.from_numpy(np.frombuffer(audio.get_raw_data(), np.int16).flatten().astype(np.float32) / 32768.0)
        audio_data = torch_audio

        # Transcribe audio to text
        text = transcribe_forever(audio_data)

        # Check for silence
        if not text:
            silence_counter += 1
            if silence_counter >= max_silence_threshold:
                print("Silence detected. Stopping recording.")
        else:
            silence_counter = 0  # Reset silence counter if speech is detected

            # Print recognized text
            print("Recognized Text:", text)

        print("Recording stopped.")
        return audio_data

 
def transcribe_forever(audio):
    audio_data = audio
    audio_model = whisper.load_model("base")
    result = audio_model.transcribe(audio_data,language='english', fp16=False) #English model

    #result = audio_model.transcribe(audio_data)

    predicted_text = result["text"]
    return predicted_text

    #result_queue.put_nowait(result) #Complete result

##################################
# PrivateGPT for query documents #
##################################

# embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")
# persist_directory = os.environ.get('PERSIST_DIRECTORY')

# model_type = os.environ.get('MODEL_TYPE')
# model_path = os.environ.get('MODEL_PATH')
# model_n_ctx = os.environ.get('MODEL_N_CTX')
# model_n_batch = int(os.environ.get('MODEL_N_BATCH',8))
# target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS',4))

# Added a paramater for GPU layer numbers
# n_gpu_layers = os.environ.get('N_GPU_LAYERS') 

class RunAI:
    def __init__(self, model_type, model_path, model_n_ctx, embeddings_model_name, persist_directory, target_source_chunks, n_gpu_layers):
        # Added custom directory path for CUDA dynamic library 
        os.add_dll_directory("C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.8/bin")
        os.add_dll_directory("C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.8/extras/CUPTI/lib64")
        os.add_dll_directory("C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.8/include")
        os.add_dll_directory("C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.8/tools")
        
        self.args = parse_arguments()  # Parse command line arguments
        embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
        chroma_client = chromadb.PersistentClient(settings=CHROMA_SETTINGS, path=persist_directory)
        db = Chroma(persist_directory=persist_directory, embedding_function=embeddings, client_settings=CHROMA_SETTINGS, client=chroma_client)
        retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})
        # callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]) if not self.args.mute_stream else CallbackManager([])
        
        # Prepare the LLM based on the model type
        if model_type == "LlamaCpp":
            self.llm = LlamaCpp(model_path=model_path, n_ctx=model_n_ctx, callback_manager=callback_manager, verbose=True, n_gpu_layers=n_gpu_layers, temperature=0.1, top_p=1, max_tokens=1000) #max_tokens=2500
        elif model_type == "GPT4All":
            self.llm = GPT4All(model=model_path, max_tokens=model_n_ctx, backend='gptj', callbacks=callback_manager, verbose=False)
        else:
            print(f"Model {model_type} not supported!")

        self.qa = RetrievalQA.from_chain_type(llm=self.llm, chain_type="stuff", retriever=retriever, return_source_documents=not self.args.hide_source)

def gpt_response(self, query):

    # Get the answer from the chain
    start = time.time()
    self.res = self.run_ai_instance.qa(query)  # Access RunAI instance using self.run_ai_instance
    self.answer, docs = self.res['result'], [] if self.run_ai_instance.args.hide_source else self.res['source_documents']
    end = time.time()

    # Print the result
    print("\n\n> Question:")
    print(query)
    print(f"\n> Answer (took {round(end - start, 2)} s.):")
    print(self.answer)

    # Print the relevant sources used for the answer
    for document in docs:
        print("\n> " + document.metadata["source"] + ":")
        print(document.page_content)
        return {'result': self.answer}
    
    return {'result': self.answer}

def parse_arguments():
    parser = argparse.ArgumentParser(description='privateGPT: Ask questions to your documents without an internet connection, '
                                                 'using the power of LLMs.')
    parser.add_argument("--hide-source", "-S", action='store_true',
                        help='Use this flag to disable printing of source documents used for answers.')

    parser.add_argument("--mute-stream", "-M",
                        action='store_true',
                        help='Use this flag to disable the streaming StdOut callback for LLMs.')

    return parser.parse_args()


############################
# Coqui for local TTS part #
############################
 

def textToSpeech(res):
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    # tts = TTS(model_name="tts_models/en/multi-dataset/tortoise-v2") #(en Male)
    tts = TTS(model_name="tts_models/en/ljspeech/vits--neon", gpu=True) #(en Female)
    tts.tts_to_file(text=res['result'])

# def input_prompt(event):
#     global text
#     if event.name.lower() == 'i':
#         text = input("What is your concern? \nPlease Enter Here: ")
#         keyboard.on_press(process_prompt)


def chosen_option(self, event, textInputed):
    global audio, text
    if event.lower() == 's':
        # self.ui.speakBtn.click()
        print('\nWHAT IS YOUR CONCERN?')
        audio = record_audio()
        return audio
        # keyboard.on_press(process_prompt_speechInput)
        
    if event.lower() == 'i':
        text = textInputed
        # process_prompt_textInput(self)

def wake_up(self, event):
    # self.ui.wakeUpBtn.click()
    
    print("Press [I] if you want to input your prompt.\n[S] For Speak.\n")
    # keyboard.on_press(chosen_option)


#after Prompt input(with text)
def process_prompt_textInput(self, textInputed):
    self.ui.process_user_input.click()
    global text
    text =  'Based on your source documents, ' + f'{textInputed}'
    self.ui.response_label.setText(f'You entered: {textInputed} [We are processing your query.]')

    if textInputed == "" or textInputed == "Please Enter your prompt here........":
        self.ui.response_label.setText("You said nothing Press [W] to wake up AMIGA again")
    else:
        # GPTresponse
        start = time.time()
        
        response = gpt_response(self, text)
        result_text = response.get('result', '')
        # print("GPT Response:", result_text)
        textGenerate = time.time()
        print(f"\n> Answer (took {round(textGenerate - start, 2)} s.):")
        # To Audio
        makeAudio = textToSpeech(response)

        temp_audio_file_path = "output.wav"

        print("Done playing.")
        self.ui.response_label.setText(result_text)
        play_audio_and_delete_file(temp_audio_file_path)
        withAudioDuration = time.time()
        print(f"\n> Answer (took {round(withAudioDuration - start, 2)} s.):")
        # return_to_wake_up()
    
    self.ui.resetBtn_2.click()
 
    
#after clickling continueBtn Prompt input(with speech)
def process_prompt_speechInput(self, textFromUser): 
    # global audio
    
    # textFromUser = self.ui.inputPrompt_2.text()
    print("You Said:", textFromUser)
    
    if textFromUser == "":
        self.ui.response_label.setText("You said nothing Press [W] to wake up AMIGO again")
    else:
        start = time.time()
        # GPTresponse
        text =  'Based on your source documents, ' + f'{textFromUser}'
        print(text)
        response = gpt_response(self, text)
        result_text = response.get('result', '')
        # print("GPT Response:", result_text)
        textGenerate = time.time()
        print(f"\n> Answer (took {round(textGenerate - start, 2)} s.):")
        # To Audio
        self.ui.response_label.setText(result_text)
        makeAudio = textToSpeech(response)

        temp_audio_file_path = "output.wav"

        play_audio_and_delete_file(temp_audio_file_path)
        print("Done playing.")
        withAudioDuration= time.time()
        print(f"\n> Answer (took {round(withAudioDuration - start, 2)} s.):")
    
    self.ui.resetBtn_2.click()

    # return_to_wake_up()        
    

# before clicking continueBtn
def transcribeAudio(self):
    global audio, text
    # if event.lower() == 'enter': 
    text = transcribe_forever(audio)
    self.ui.inputPrompt_2.setText(f'{text}')
    self.ui.msg_label4.setText("You Said")
    self.ui.inputPrompt_2.setReadOnly(False)


def load_speech_page(self):
   
    print("Loading speech page...")
    self.ui.continueBtn.setEnabled(False)
    self.ui.continueBtn.setText("Disabled")
    
    textFromUser = self.ui.inputPrompt_2.text()
    self.ui.response_label.setText(f'You Said: {textFromUser} [We are processing your query.]')
    
    print("done running")
    # process_prompt_textInput(self, textFromUser)
    
        
        
        
        
# Function to delete the output.wav file
def delete_output_file():
    try:
        os.remove("output.wav")
        print("Output file deleted successfully.")
    except FileNotFoundError:
        print("Output file not found.")
    except Exception as e:
        print("Error occurred while deleting the output file:", e)
        
# Function to play audio and delete the file afterward
def play_audio_and_delete_file(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Wait until the audio finishes playing
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)  # Sleep for a short duration before checking again
        
    # Unload the music to release the lock on the file
    pygame.mixer.music.unload()

    delete_output_file()  # Delete the output.wav file after playing

def return_to_wake_up():
    text = ''
    # keyboard.unhook_all()  # Remove all hooks to avoid conflicts
    # print("Please Enter [W] to wake up AMIGO")
    # keyboard.on_press(wake_up) 
    
# def record_audio():
#     print("currently recording")
#     #load the speech recognizer and set the initial energy threshold and pause threshold
#     r = sr.Recognizer()
#     r.energy_threshold = 300
#     r.pause_threshold = 0.8
#     r.dynamic_energy_threshold = False

#     with sr.Microphone(sample_rate=16000) as source:
#         i = 0
#         #get and save audio to wav file
#         audio = r.listen(source)
#         torch_audio = torch.from_numpy(np.frombuffer(audio.get_raw_data(), np.int16).flatten().astype(np.float32) / 32768.0)
#         audio_data = torch_audio

#         return audio_data