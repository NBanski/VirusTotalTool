import tkinter as tk
import tkinter.scrolledtext as stxt

from modules.gui.darkMotive import dframe, dbutton, dlabel, dpage

class filesPage(dpage):
    def __init__(self, *args, **kwargs):
        dpage.__init__(self, *args, **kwargs)
        
        bLoadFile = dbutton(self,
        text="Load files")

        fileBox = stxt.ScrolledText(self, 
        fg="white", 
        bg="gray15",
        insertofftime=0,
        width=40,
        height=40,
        wrap="none",
        insertbackground="white",
        )

        resultBox = stxt.ScrolledText(self, 
        fg="white", 
        bg="gray15",
        insertofftime=0,
        width=80,
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

        bLoadFile.grid(row=0, column=0)

        fileBox.grid(row=1, column=0)
        resultBox.grid(row=1, column=1)

        bFileInfo.grid(row=2, column=0)
        bFileReport.grid(row=2, column=1)
        bFileScan.grid(row=2, column=2)

        

