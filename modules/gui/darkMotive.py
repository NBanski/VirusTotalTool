import tkinter as tk

# Changing default elements of the GUI to fit the "dark" motive.

# dbutton stands for dark button.
class dbutton(tk.Button):
    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self["activebackground"] = "red"
        self["bg"] = "gray15"
        self["fg"] = "white"
        self["width"] = "20"
        self["height"] = "2"

# dlabel stand for dark label.
class dlabel(tk.Label):
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self["bg"] = "gray15"
        self["fg"] = "white"

# dpage stands for dark page.
class dpage(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self["bg"] = "gray15"
    # This is for switching pages in application.
    def show(self):
        self.lift()
        
# frame stands for dark frame.

class dframe(tk.Frame):
    def __init__(self, *args, **kwagrs):
        tk.Frame.__init__(self)
        self["bg"] = "gray15"