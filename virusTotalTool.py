import tkinter as tk

from modules.local.settings import startConfigFiles, startDatabase
from modules.gui.mainWindow import mainFrame

if __name__ == "__main__":
    startConfigFiles()
    startDatabase()    
    root = tk.Tk()
    main = mainFrame(root)
    title = root.title("Virus Total Tool")
    main.pack(side="top", fill="both", expand=True)
    root.resizable(0, 1)
    root.mainloop()

# to do: extract file report and put it into gui