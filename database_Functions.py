import os
import sys
from src.ui_interface import *
from src.ui_interface import Ui_MainWindow
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
###################################
#import sqlite3
import sqlite3
from sqlite3 import Error

class DatabaseFunctions:
    def __init__(self, ui):
        self.ui = ui
        self.conn = None
        self.cur = None

    def open_connection(self):
        try:
            self.conn = sqlite3.connect("db/userPromptList_DB.db")
            self.cur = self.conn.cursor()

            # Create the Users table if it doesn't exist
            self.cur.execute('''CREATE TABLE IF NOT EXISTS Users(INPUT_ID INTEGER PRIMARY KEY AUTOINCREMENT, INPUT_PROMPT TEXT)''')
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error connecting to the database:", e) 
            
    def close_connection(self):
        try:
            if self.cur:
                self.cur.close()
            if self.conn:
                self.conn.close()
        except sqlite3.Error as e:
            print("Error closing connection:", e)

    def display_inputPrompt(self):
        input_data = []
        try:
            if not self.conn:
                self.open_connection()
                
            self.cur.execute("SELECT INPUT_ID, INPUT_PROMPT FROM Users")
            input_data = self.cur.fetchall()
        except sqlite3.Error as e:
            print("Error fetching input prompts:", e)
            
        return input_data
    
    def add_inputPrompt(self, userPrompt):
        try:
            if not userPrompt:
                print("no user input")
                return
            
            if not self.conn:
                self.open_connection()
            
            self.cur.execute("INSERT INTO Users(INPUT_PROMPT) VALUES (?)", (userPrompt,))
            self.conn.commit()
            
            # After adding the new input prompt, load the updated data
            input_prompt_data = self.display_inputPrompt()
            self.load_data(input_prompt_data)
        
        except sqlite3.Error as e:
            print("Error adding input prompt:", e)

    def load_data(self, input_data):
        try:
            self.ui.userInputTableWidget.setRowCount(len(input_data))
            for row, userPrompt in enumerate(input_data):
                self.ui.userInputTableWidget.setItem(row, 0, QTableWidgetItem(str(userPrompt[0])))
                self.ui.userInputTableWidget.setItem(row, 1, QTableWidgetItem(userPrompt[1]))
        except Exception as e:
            print("Error loading data:", e)
    
    def clear_database(self):
        try:
            if not self.conn:
                self.open_connection()
                
            self.cur.execute("DELETE FROM Users")
            self.conn.commit()
            
            print("Database cleared successfully.")
            # After adding the new input prompt, load the updated data
            input_prompt_data = self.display_inputPrompt()
            self.ui.userInputTableWidget.clearContents()
            self.load_data(input_prompt_data)
            
        except sqlite3.Error as e:
            print("Error adding input prompt:", e)
    
    # def clear_database(self):
    #     try:
    #         conn = sqlite3.connect("db/userPromptList_DB.db")
    #         cur = conn.cursor()
    #         cur.execute("DELETE FROM Users")
    #         conn.commit()
    #         print("Database cleared successfully.")
    #         # Close the connection
    #         cur.close()
    #         conn.close()
    #     except sqlite3.Error as e:
    #         print("Error clearing database:", e)    
    #     # After adding the new input prompt, load the updated data
    #     input_prompt_data = self.display_inputPrompt()
    #     print(input_prompt_data)
    #     # self.load_data(input_prompt_data)
    
        
            
def get_UserPrompt(self, TextInputted):
    Prompt = TextInputted
    # email = self.email.text()
    # phoneNumber = self.phoneNumber.text()
    db_functions = DatabaseFunctions(self.ui)
    db_functions.add_inputPrompt(Prompt)
    
    # appFunctions.display_users()
    
    
    