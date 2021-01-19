import tkinter as tk

from modules.local.settings import startConfigFiles, startDatabase
from modules.gui.mainWindow import mainFrame

# To do: create database configuration file to be used during second and later logins.
# It should be created on first login.

if __name__ == "__main__":
    startConfigFiles()
    startDatabase()    
    root = tk.Tk()
    main = mainFrame(root)
    title = root.title("Virus Total Tool")
    main.pack(side="top", fill="both", expand=True)
    root.resizable(0, 1)
    root.mainloop()