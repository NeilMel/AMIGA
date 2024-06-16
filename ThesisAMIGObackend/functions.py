
########################################################################
# IMPORT GUI FILE
from tkinter import messagebox
from src.ui_interface import Ui_MainWindow
from PySide6.QtWidgets import QMessageBox
########################################################################
#import privateGPT_Voice
from privateGPT_Voice import *
########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
########################################################################
import time
import threading
from PySide6.QtCore import QTimer

#######
#import database funtions
from database_Functions import get_UserPrompt




class BackendFunctions(Ui_MainWindow):
    
    pageCtr = 0
    chose_option_byUser = ''
    
    #Page Navigation
    def getKeyPressed(self, event):
        
        if (event.lower() == 'a') and BackendFunctions.pageCtr == 0:
            BackendFunctions.pageCtr = 5
            print("At Admin Page")
            
        if (event.lower() == 'w') and BackendFunctions.pageCtr == 0:
            self.ui.adminBtn.setText("Disabled")
            self.ui.adminBtn.setEnabled(False)
            PageCounter()
            wakeUp_AI(self, event)
        
        if (event.lower() == 'i') and BackendFunctions.pageCtr == 1:
            BackendFunctions.chose_option_byUser = 'i' #get the chosen option
            self.ui.resetBtn.setText("Disabled")
            self.ui.resetBtn.setEnabled(False)
            PageCounter()
            inputPromptPage(self, event)
            
        if (event.lower() == 's') and BackendFunctions.pageCtr == 1:
            BackendFunctions.chose_option_byUser = 's' #get the chosen option
            self.ui.resetBtn.setText("Disabled")
            self.ui.resetBtn.setEnabled(False)
            PageCounter()
            speakPromptPage(self, event)
            
        if event.lower() == 'enter' and BackendFunctions.pageCtr == 2:
            PageCounter()
            if (BackendFunctions.chose_option_byUser == 'i'):
                textInputed = self.ui.inputPrompt.text()
                chosen_option(self, event='i', textInputed=textInputed)
                process_prompt_textInput(self, textInputed)
                get_UserPrompt(self, textInputed)
                BackendFunctions.resetPage(self, True)
                
            if (BackendFunctions.chose_option_byUser == 's'):
                transcribeAudio(self)
                print(f'you entered: to be processed to Speak')    
                
        #for the processing of audio
        if event.lower() == 'enter' and BackendFunctions.chose_option_byUser == 's' and BackendFunctions.pageCtr == 3:
            PageCounter()
            self.ui.continueBtn.setEnabled(True)
            self.ui.continueBtn.setText("Continue")
        
        # #for Gpt Response
        if event.lower() == 'continue' and BackendFunctions.chose_option_byUser == 's' and BackendFunctions.pageCtr == 4:
            self.ui.process_speak_input.click()
            print("above run first")
            load_speech_page(self)
            PageCounter() # Increment page counter
            # Schedule the next action to run after a delay
            textFromUser = self.ui.inputPrompt_2.text()
            run_after_delay(self, 1, lambda: run_after_prompt(self, textFromUser))
            
    #end of page navigation
    
    
    #for the page reset function     
    def resetPage(self, pageReset):
        if(pageReset):
            BackendFunctions.pageCtr = 0
            BackendFunctions.chose_option_byUser = '' 
            reset_all_btn(self)
            reset_all_label(self)
            reset_all_input(self)
            return_to_wake_up() #reset ai
            self.ui.resetBtn_2.click()
    #end of page reset funtion
        
    
    #function for admin verification
    def adminLogin(self):
          
        username = self.ui.usernamefield.text()
        password = self.ui.passwordfield.text()
        
        if username != "CITUadmin" and password != "123AmigoAdmin123":
            isAdmin = False
            show_popup(self, isAdmin)
        else:
            isAdmin = True
            show_popup(self, isAdmin)
            

          
def run_after_delay(self, delay, function):
    timer = QTimer(self)
    timer.setSingleShot(True)
    timer.timeout.connect(function)
    timer.start(delay * 1000)  # QTimer works with milliseconds, so we convert seconds to milliseconds

def run_after_prompt(self, textFromUser):
    # Start the time-consuming task in a new thread
    thread = threading.Thread(target=process_prompt_speechInput, args=(self, textFromUser))
    get_UserPrompt(self, textFromUser)
    thread.start()
    
    # Optionally, you can join the thread to wait for its completion
    # thread.join()

    # Reset the page after the task is completed
    BackendFunctions.resetPage(self, True)
            
            
def wakeUp_AI(self, event):
    self.ui.wakeUpBtn.click()
    # wake_up(self, event)

def inputPromptPage(self, event):
    if event.lower() == 'i':
        self.ui.inputBtn.click()

    
def speakPromptPage(self, event):
    self.ui.speakBtn.click()
    chosen_option(self, event='s', textInputed='')
        
def adminPage (self, event):
    self.ui.adminBtn.click()
    
def dashboardPage(self):
    self.ui.loginBtn.click()
    
# for the Pages
def PageCounter():
    if(BackendFunctions.pageCtr >= 0 and BackendFunctions.pageCtr <= 7):
        BackendFunctions.pageCtr +=1
    return BackendFunctions.pageCtr
    
def resetPageCtr():
    BackendFunctions.pageCtr = 0
    return BackendFunctions.pageCtr


def show_popup(self, isAdmin):
    
    if isAdmin == False:  
        msg = QMessageBox()
        msg.setWindowTitle("Login Error")
        msg.setText("Incorrect Username or Password Please Try again!")
        msg.setIcon(QMessageBox.Warning)
    else:
        self.ui.adminBtn.setEnabled(False)
        self.ui.adminBtn.setText("Welcome Admin")
        msg = QMessageBox()
        msg.setWindowTitle("Login Success!")
        msg.setText("Welcome Admin!")
        msg.setIcon(QMessageBox.Information)
        
        self.ui.logInPageBtn.click()
    
    x = msg.exec_()

def ingest_popup(self):
    
    msg = QMessageBox()
    msg.setWindowTitle("Ingesting Files")
    msg.setText("Ingesting files. This might take a while Please Wait!")
    msg.setIcon(QMessageBox.Warning)
    
    x = msg.exec_()
    
def done_ingest_popup(self):
    
    msg = QMessageBox()
    msg.setWindowTitle("Ingesting Files")
    msg.setText("Ingestion complete! You can now run AMIGO-AI to query your documents")
    msg.setIcon(QMessageBox.Warning)
    
    x = msg.exec_()
        
def reset_all_label(self):
    self.ui.msg_label4.setText("Press 'Enter' if you're done")
    
def reset_all_btn(self):
    self.ui.resetBtn.setEnabled(True)
    self.ui.adminBtn.setEnabled(True)
    self.ui.adminBtn.setText("Admin")
    self.ui.resetBtn.setText("Reset")
    self.ui.continueBtn.setEnabled(False)
    self.ui.continueBtn.setText("Disabled")
      
def reset_all_input(self):
    self.ui.inputPrompt_2.setText("[PLEASE NOTE: This will only stop and the idle timer is less than '0' or the user would click 'ENTER']")
    self.ui.inputPrompt_2.setReadOnly(True)
    self.ui.inputPrompt.setText("Please Enter your prompt here........")
    self.ui.usernamefield.setText("")
    self.ui.passwordfield.setText("")
    


    
    