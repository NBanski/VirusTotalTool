import tkinter as tk
import tkinter.scrolledtext as stxt

from tkinter.filedialog import askopenfilenames
from modules.gui.darkMotive import dframe, dbutton, dlabel, dpage

class filesPage(dpage):
    def __init__(self, *args, **kwargs):
        dpage.__init__(self, *args, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # File boxes.

        fileBox = stxt.ScrolledText(self, 
        fg="white", 
        bg="gray15",
        insertofftime=0,
        width=80,
        height=40,
        wrap="none",
        insertbackground="white",
        state="disabled"
        )

        # Define variables for later use.
        filePaths = []

        # Logic for file loading.

        def askForFilePath():
            pathsTuple = askopenfilenames()
            pathsList = list(pathsTuple)
            # To clean up a list after populating.
            filePaths.clear()
            # To populate a list again.
            for path in pathsList:
                filePaths.append(path)
            # Updating initial prompt.
            fileBox.configure(state="normal")
            fileBox.delete(1.0, tk.END)
            fileBox.insert(tk.END, "Files supplied:")
            fileBox.configure(state="disabled")

        # Button to load file.

        bLoadFile = dbutton(self,
        text="Load files",
        command=askForFilePath)

        # Logic to getting information about files.
        
        def getFilesInfo():
            infoPaths = filePaths

        # Buttons to operate on file.

        bFileInfo = dbutton(self,
        text="Get info",
        command=getFilesInfo)

        bFileReport = dbutton(self,
        text="Get reports")

        bFileScan = dbutton(self,
        text="Scan files")

        # Loading widgets to interface.

        bLoadFile.grid(row=0, column=1, pady=(15))

        fileBox.grid(row=1, column=0, padx=(20,0), columnspan=3)

        bFileInfo.grid(row=2, column=0, padx=(10), pady=(20), sticky="E")
        bFileReport.grid(row=2, column=1, padx=(10), pady=(20),)
        bFileScan.grid(row=2, column=2, padx=(10), pady=(20), sticky="W")