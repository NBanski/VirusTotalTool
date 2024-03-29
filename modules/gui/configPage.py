import tkinter as tk
import os

from modules.gui.darkMotive import dbutton, dlabel, dpage
from modules.local.databaseBasic import executeSchema
from modules.local.settings import setApi
from modules.network.proxy import turnProxy

class configPage(dpage):
    def __init__(self, *args, **kwargs):
        dpage.__init__(self, *args, **kwargs)

        def openWarningWindow():
            warningWindow = tk.Tk()
            warningWindow["bg"] = "gray15"
            warningWindow.title("You absolute madman!")
            warningWindow.geometry("400x180")
            warningWindow.resizable(0, 0)
            dlabel(warningWindow, text="""This action will erase the database (if it exists), and create a new one.
PROCEED WITH CAUTION. THINK ABOUT BACKING UP THE BASE.
Do you still want to do this?"""
            ).pack(padx=20, pady=25)

            def closeWarningWindow():
                warningWindow.destroy()

            b1_no = dbutton(warningWindow, text="No", command=closeWarningWindow)
            b2_yes = dbutton(warningWindow, text="Yes", command=lambda:[executeSchema(), closeWarningWindow()])    

            b1_no.pack(side="right", padx=30)
            b2_yes.pack(side="top", padx=30)

        def open_change_api_window():
            change_window = tk.Tk()
            change_window["bg"] = "gray15"
            change_window.title("Change API Key")
            change_window.geometry("510x100")
            change_window.resizable(0, 0)

            def close_change_api_window():
                change_window.destroy()

            apiLabel = dlabel(change_window, text="Enter API Key:")
            apiLabel.grid(column=0, row=0, padx=(10,0), pady=(20, 0))

            apiEntry = tk.Entry(change_window, bg="gray15", fg="white", width=65, show="*") 
            apiEntry.grid(column=1, row=0, padx=(10,0), pady=(20, 0))

            apiChange = dbutton(change_window, text="Change!", command=lambda:[setApi(apiEntry.get()), close_change_api_window()])
            apiChange.grid(column=1, row=1, pady=(10, 10))       

        def openProxySettings():
            proxyWindow = tk.Tk()
            proxyWindow["bg"] = "gray15"
            proxyWindow.title("Proxy settings")
            proxyWindow.resizable(0, 1)

            loginLabel = dlabel(proxyWindow, text="Enter login:")
            passwordLabel = dlabel(proxyWindow, text="Enter password:")
            addressLabel = dlabel(proxyWindow, text="Enter proxy address:")
            portLabel = dlabel(proxyWindow, text="Enter proxy port:")

            loginEntry = tk.Entry(proxyWindow, bg="gray15", fg="white", width=55)
            passwordEntry = tk.Entry(proxyWindow, bg="gray15", fg="white", width=55, show="*")
            addressEntry = tk.Entry(proxyWindow, bg="gray15", fg="white", width=55)
            portEntry = tk.Entry(proxyWindow, bg="gray15", fg="white", width=55)
            
            
            def closeProxySettings():
                turnProxy("on")
                pxUser = loginEntry.get()
                pxPassword = passwordEntry.get()
                pxAddress = addressEntry.get()
                pxPort = portEntry.get()
                proxyWindow.destroy()   

            bSetProxyConfiguration = dbutton(proxyWindow,
            text="Configure!",
            command=closeProxySettings)

            loginLabel.pack(side="top", pady=(10,0))
            loginEntry.pack(side="top")
            passwordLabel.pack(side="top")
            passwordEntry.pack(side="top")
            addressLabel.pack(side="top")
            addressEntry.pack(side="top")
            portLabel.pack(side="top")
            portEntry.pack(side="top")
            bSetProxyConfiguration.pack(side="top", pady=(10, 10))

        def disableProxy():
            turnProxy("off")

        b1ResetDatabase = dbutton(self, 
        text="Reset database",
        command=openWarningWindow
        )

        b2ChangeApi = dbutton(self,
        text="Change API Key",
        command=open_change_api_window
        )

        setProxy = dbutton(self,
        text="Set proxy server.",
        command=openProxySettings
        )

        b4Placeholder = dbutton(self,
        text="Disable proxy.",
        command=disableProxy
        )

        b1ResetDatabase.grid(column=0, row=1, padx=(450, 300), pady=(250, 10))
        b2ChangeApi.grid(column=0, row=2, padx=(450, 300), pady=(0, 10))
        setProxy.grid(column=0, row=3, padx=(450, 300), pady=(0, 10))
        b4Placeholder.grid(column=0, row=4, padx=(450, 300), pady=(0, 10))