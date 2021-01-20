import tkinter as tk
import tkinter.scrolledtext as stxt

from modules.gui.darkMotive import dframe, dbutton, dlabel, dpage

class filesPage(dpage):
    def __init__(self, *args, **kwargs):
        dpage.__init__(self, *args, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        bLoadFile = dbutton(self,
        text="Load files")

        fileBox = stxt.ScrolledText(self, 
        fg="white", 
        bg="gray15",
        insertofftime=0,
        width=50,
        height=40,
        wrap="none",
        insertbackground="white",
        )

        resultBox = stxt.ScrolledText(self, 
        fg="white", 
        bg="gray15",
        insertofftime=0,
        width=50,
        height=40,
        wrap="none",
        state="disabled"
        )

        # Buttons.

        bFileInfo = dbutton(self,
        text="Get info")

        bFileReport = dbutton(self,
        text="Get report")

        bFileScan = dbutton(self,
        text="Scan files")

        # Loading to interface.

        bLoadFile.grid(row=0, column=1, pady=(15))

        fileBox.grid(row=1, column=0, padx=(20,0))
        resultBox.grid(row=1, column=2, padx=(0,20), sticky="W")

        bFileInfo.grid(row=2, column=0, padx=(10), pady=(20), sticky="E")
        bFileReport.grid(row=2, column=1, padx=(10), pady=(20),)
        bFileScan.grid(row=2, column=2, padx=(10), pady=(20), sticky="W")

        

