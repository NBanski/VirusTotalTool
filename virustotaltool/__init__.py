import tkinter as tk
from interface.mainWindow import mainWindow

if __name__ == "__main__":
    root = tk.Tk()
    main = mainWindow(root)
    title = root.title("VirusTotalTool")
    main.pack(side="top", fill="both", expand=True)
    root.resizable(0, 0)
    root.mainloop()