########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
import shutil
########################################################################
# IMPORT GUI FILE
from src.ui_interface import *
from PySide6.QtWidgets import QFileDialog
from ingest import main
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
########################################################################
from PySide6.QtCore import QTimer, Qt

# import Keyboard
import keyboard
from ThesisAMIGObackend.functions import BackendFunctions, ingest_popup, done_ingest_popup, gpt_response
from database_Functions import DatabaseFunctions
import time
from privateGPT_Voice import RunAI

# backEndFunct = backend_functions()
########################################################################

########################################################################
## MAIN WINDOW CLASS
######################################################################## 
embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")
persist_directory = os.environ.get('PERSIST_DIRECTORY')

model_type = os.environ.get('MODEL_TYPE')
model_path = os.environ.get('MODEL_PATH')
model_n_ctx = os.environ.get('MODEL_N_CTX')
model_n_batch = int(os.environ.get('MODEL_N_BATCH',8))
target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS',4))
n_gpu_layers = os.environ.get('N_GPU_LAYERS') 

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        # QMainWindow.__init__(self)
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        
        self.run_ai_instance = RunAI(model_type, model_path, model_n_ctx, embeddings_model_name, persist_directory, target_source_chunks, n_gpu_layers)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        #Use this if you only have one json file named "style.json" inside the root directory, "json" directory or "jsonstyles" folder.
        # loadJsonStyle(self, self.ui) 

        # Use this to specify your json file(s) path/name
        loadJsonStyle(self, self.ui, jsonFiles = {
            "json-styles/style.json"
            }) 

        ########################################################################

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show() 

        ########################################################################
        # UPDATE APP SETTINGS LOADED FROM JSON STYLESHEET 
        # ITS IMPORTANT TO RUN THIS AFTER SHOWING THE WINDOW
        # THIS PROCESS WILL RUN ON A SEPARATE THREAD WHEN GENERATING NEW ICONS
        # TO PREVENT THE WINDOW FROM BEING UNRESPONSIVE
        ########################################################################
        # self = QMainWindow class
        QAppSettings.updateAppSettings(self)
        
        #hide some Buttons
        self.ui.resetBtn_2.hide()
        self.ui.wakeUpBtn.hide()
        self.ui.process_user_input.hide()
        self.ui.process_speak_input.hide()
        self.ui.logInPageBtn.hide()
        self.ui.continueBtn.setText("Disabled")
        
        self.backEndFunct = BackendFunctions()
        #start Database
        self.DbFunctions = DatabaseFunctions(self.ui)
        
        
        #redirect to admin Page
        self.ui.adminBtn.clicked.connect(lambda: BackendFunctions.getKeyPressed(self, 'a'))
        
        #verify if user is admin using LoginBtn
        self.ui.loginBtn.clicked.connect(lambda: BackendFunctions.adminLogin(self))
        
        # Connect the clicked signal of resetBtn to the reset_timer slot
        self.ui.resetBtn.clicked.connect(self.reset_timer)
        
        #if user done with text edit from Speech input
        self.ui.continueBtn.clicked.connect(lambda: BackendFunctions.getKeyPressed(self, event='continue'))
        
        #remove all data inputted
        self.ui.deleteDataBtn.clicked.connect(self.DbFunctions.clear_database)
        
        keyboard.on_press(lambda event: self.userClicked(event))
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Timer interval in milliseconds
        
        self.seconds = 1200
        # print(f"Timer: {self.seconds} seconds")
        
        MainWindow.pageReset = False
        
        #embed here
        self.ui.embedBtn.clicked.connect(self.run_ingestion)
        self.ui.browseOrdeleteBtn.clicked.connect(self.browseFiles)
        self.getFileList()
        
        #load data
        input_prompt_data = self.DbFunctions.display_inputPrompt()
        self.DbFunctions.load_data(input_prompt_data)
        # self.DbFunctions.close_connection()
        
        
        
    
    
    def update_timer(self):
        self.seconds -= 1
        self.ui.idleTimer.display(self.seconds)
        
        if self.seconds == 0:
            BackendFunctions.resetPage(self, True)
            # BackendFunctions.getKeyPressed(self, 'enter')
        if self.seconds <=-1:
            self.ui.idleTimer.display("SLEEP")
                       
    # Define the reset_timer slot
    def reset_timer(self):
        self.seconds = 0
        BackendFunctions.resetPage(self, True)
            
    def userClicked(self, event):
        # get the key that is pressed
        key = event.name
        if (key):
            setEvent = key.lower()
        # print(f'At userClicked {setEvent}')
        self.seconds = 1200
        BackendFunctions.getKeyPressed(self, setEvent)
        
    #for browsing files
    def getFileList(self):
        directory = "source_documents"
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, directory)
        dir_list = os.listdir(path)
        print("Files and directories before in '", path, "' :")
        print(dir_list)
        
        # Format the list of filenames as individual lines
        file_list_formatted = '\n'.join(dir_list)
        
        # Set the formatted list as the text of the label
        self.ui.fileListLbl.setText(file_list_formatted)
            
    def browseFiles(self):
        directory = "source_documents"
        cwd_path = os.path.join(os.getcwd(), directory)
        formats = "Data Files (*.pdf *.docx *.ppt *.pptx *.txt);;All Files (*)"

        # Create a file dialog and make it modal
        dialog = QFileDialog(self)
        dialog.setModal(True)
        
        # Get the selected file name and file type filter
        fname, _ = dialog.getSaveFileName(self, 'Save File', cwd_path, formats)

        # Check if a file name is selected
        if fname:
            # Get the path of the selected file
            selected_file_path = os.path.abspath(fname)

            try:
                # Create the "source_documents" directory if it doesn't exist
                os.makedirs(cwd_path, exist_ok=True)
                
                # copy the selected file to the "source_documents" directory
                shutil.copy(selected_file_path, cwd_path)
                
                # Update the label to display the selected file path
                self.getFileList()
                
            except Exception as e:
                # Display an error message if any error occurs
                print("Error:", e)
                self.getFileList()
    #End for browsing files
    
    #embed file
    def run_ingestion(self):
        ingest_popup(self)
        start = time.time()
        main()
        ingestionTime = time.time()
        print(f"\n> Ingestion (took {round(ingestionTime - start, 2)} s.):")
        done_ingest_popup(self)
    #end embed file
    
    



        

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  

