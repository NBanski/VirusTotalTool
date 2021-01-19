import tkinter as tk

from modules.gui.darkMotive import dbutton, dlabel, dpage, dframe
from modules.gui.reportsPage import reportsPage
from modules.gui.scansPage import scansPage
# from modules.gui.filesPage import filesPage
from modules.gui.historyPage import historyPage
# from modules.gui.configPage import configPage


class mainFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = reportsPage(self)
        p2 = scansPage(self)
        # p3 = filesPage(self)
        p4 = historyPage(self)
        # p5 = configPage(self)

        # Navbar buttons frame settings. 

        buttonframe = dframe(self)
        buttonframe.pack(side="top", fill="x", expand="False")

        # Topmost container.
        
        container = tk.Frame(self)
        container.config(height="800", width="1000")
        container.pack(side="top", fill="both", expand="True")

        # Top navbar buttons settings.

        b1 = dbutton(buttonframe, text="URL report", command=p1.lift)
        b2 = dbutton(buttonframe, text="URL scan", command=p2.lift)
        b3 = dbutton(buttonframe, text="File scan" """ command=p3.lift """)
        b4 = dbutton(buttonframe, text="Search history", command=p4.lift)
        b5 = dbutton(buttonframe, text="Settings" """ command=p5.lift """)

        # Top navbar buttons packing.

        b1.pack(side="left", padx=(125,10), pady=(10,10))
        b2.pack(side="left", padx=(0, 10), pady=(10,10))
        b3.pack(side="left", padx=(0, 10), pady=(10,10))
        b4.pack(side="left", padx=(0, 10), pady=(10,10))
        b5.pack(side="left", padx=(0,125), pady=(10,10))

        # Packing pages in container (mainframe).

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        # p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        # p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        p1.show()