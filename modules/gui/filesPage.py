import tkinter as tk
import tkinter.scrolledtext as stxt
from time import sleep 

from tkinter.filedialog import askopenfilenames
from modules.gui.darkMotive import dframe, dbutton, dlabel, dpage
from modules.local.fileOperations import getFileSize, getFileName, getFileMimeEncoding, hashFile
from modules.local.databaseOperations import insertFileReport, extractReportByHash
from modules.network.apiRequests import getFileScan

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
            fileBox.insert(tk.END, "Files supplied:\n")
            for path in filePaths:
                fileBox.insert(tk.END, (path + "\n"))
            fileBox.configure(state="disabled")

        # Button for loading file.

        bLoadFile = dbutton(self,
        text="Load files",
        command=askForFilePath)

        # Logic for getting information about files.
        
        beautyBreaker = "---------------------------------------------------------\n"

        def getFilesInfo():
            infoPaths = filePaths
            fileBox.configure(state="normal")
            fileBox.delete(1.0, tk.END)
            fileBox.insert(tk.END, beautyBreaker)
            for element in infoPaths:
                fileBox.insert(tk.END, (str(getFileName(element)) + "\n"))
                fileBox.insert(tk.END, (str(getFileSize(element)) + "\n"))
                fileBox.insert(tk.END, (str(getFileMimeEncoding(element)) + "\n"))
                fileBox.insert(tk.END, (str(hashFile(element)) + "\n"))
                fileBox.insert(tk.END, beautyBreaker)
            fileBox.configure(state="disabled")

        # Logic for getting reports about files.

        def getFilesReport():
            reportPaths = filePaths
            for element in reportPaths:
                elementHash = hashFile(element)
                insertFileReport(elementHash)
            fileBox.configure(state="normal")
            fileBox.delete(1.0, tk.END)
            fileBox.insert(tk.END, beautyBreaker)
            for element in reportPaths:
                elementHash = hashFile(element)
                fileBox.insert(tk.END, (str(getFileName(element)) + "\n"))
                fileBox.insert(tk.END, (str(getFileSize(element)) + "\n"))
                fileBox.insert(tk.END, (str(extractReportByHash(elementHash)) + "\n"))
                fileBox.insert(tk.END, (elementHash + "\n"))
                fileBox.insert(tk.END, beautyBreaker)
            fileBox.configure(state="disabled")

        # Logic for sending file to a server.

        def scanFiles():
            tempHashes = []
            scanPaths = filePaths
            fileBox.configure(state="normal")
            fileBox.delete(1.0, tk.END)
            fileBox.insert(tk.END, beautyBreaker)
            fileBox.insert(tk.END, "Sending files now...\n")
            fileBox.insert(tk.END, beautyBreaker)
            fileBox.configure(state="disabled")
            sleep(1)
            for path in scanPaths:
                response = getFileScan(path)
                tempHash = response.json()
                tempHash = tempHash.get('sha256')
                tempName = getFileName(path)
                tempHashes.append(tempHash)
                fileBox.configure(state="normal")
                fileBox.insert(tk.END, tempName + "\n")
                fileBox.insert(tk.END, "Sent.\n")
                fileBox.insert(tk.END, beautyBreaker)
                fileBox.configure(state="disabled")
            fileBox.configure(state="normal")
            fileBox.insert(tk.END, "Now wait for the results. \nIt may take some time; try to fetch reports after.\n")
            fileBox.insert(tk.END, beautyBreaker)
            fileBox.configure(state="disabled")

        def fileScanWarning():
            warningWindow = tk.Tk()
            warningWindow["bg"] = "gray15"
            warningWindow.title("Warning!")
            warningWindow.geometry("450x150")
            warningWindow.resizable(0, 0)

            warningText = '''File size limit is 32 MB.
Keep in mind that these files will be stored on VT servers. .
Are you sure they do not contain data sensitive for you or your organisation?'''

            def closeWarningWindowNo():
                warningWindow.destroy()

            def closeWarningWindowYes():
                warningWindow.destroy()
                scanFiles()


            warningLabel = dlabel(warningWindow, text=warningText, justify="center")
            warningButtonYes = dbutton(warningWindow, text="Yes", command=closeWarningWindowYes)
            warningButtonNo = dbutton(warningWindow, text="No", command=closeWarningWindowNo)

            warningLabel.pack(padx=20, pady=20)
            warningButtonYes.pack(side="left", padx=(50, 10), pady=(0, 10))
            warningButtonNo.pack(side="right", padx=(10, 50), pady=(0, 10))
  

        # Buttons for operating on files.

        bFileInfo = dbutton(self,
        text="Get info",
        command=getFilesInfo)

        bFileReport = dbutton(self,
        text="Get reports",
        command=getFilesReport)

        bFileScan = dbutton(self,
        text="Scan files",
        command=fileScanWarning)

        # Loading widgets to interface.

        bLoadFile.grid(row=0, column=1, pady=(15))

        fileBox.grid(row=1, column=0, padx=(20,0), columnspan=3)

        bFileInfo.grid(row=2, column=0, padx=(10), pady=(20), sticky="E")
        bFileReport.grid(row=2, column=1, padx=(10), pady=(20),)
        bFileScan.grid(row=2, column=2, padx=(10), pady=(20), sticky="W")