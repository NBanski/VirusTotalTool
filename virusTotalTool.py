import tkinter as tk
from modules.local.settings import startConfigFiles, startDatabase

# To do: create database configuration file to be used during second and later logins.
# It should be created on first login.

# if __name__ == "__main__":
#     first_start()
#     root = tk.Tk()
#     main = main_window(root)
#     title = root.title("Virus Total API Tool")
#     main.pack(side="top", fill="both", expand=True)
#     root.resizable(0, 0)
#     root.mainloop()

startConfigFiles()
startDatabase()