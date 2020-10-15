import tkinter as tk

# Single dark page.
class page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self["bg"] = "gray15"
    def show(self):
        self.lift()

# Single dark button.
class dbutton(tk.Button):
    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self["activebackground"] = "red"
        self["bg"] = "gray15"
        self["fg"] = "white"
        self["width"] = "20"
        self["height"] = "2"

# Single default label.
class dlabel(tk.Label):
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self["bg"] = "gray15"
        self["fg"] = "white"