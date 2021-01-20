from tkinter.filedialog import askopenfilenames

def askForFilePath():
    path = askopenfilenames()
    return path