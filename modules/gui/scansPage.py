import tkinter as tk
import tkinter.scrolledtext as stxt
import time

from modules.gui.darkMotive import dframe, dbutton, dlabel, dpage
from modules.local.databaseOperations import insertReport, extractReportById, queryUrlScan

class scansPage(dpage):
   def __init__(self, *args, **kwargs):
       dpage.__init__(self, *args, **kwargs)

       url_box = stxt.ScrolledText(self, 
       fg="white", 
       bg="gray15",
       insertofftime=0,
       width=40,
       height=40,
       wrap="none",
       insertbackground="white",
       )

       result_box = stxt.ScrolledText(self, 
       fg="white", 
       bg="gray15",
       insertofftime=0,
       width=80,
       height=40,
       wrap="none",
       state="normal"
       )

       instruction = dlabel(self, 
       text="""Insert URLS which you want to scan into the left box. Result will appear in the right box.
Acceptable format is <domain name>.<extension>. Do not use any protocol prefixes.""",
       justify="left"
       )

       def get_urls():
            urls = url_box.get("1.0", "end-1c").split("\n")
            result_box.configure(state="normal")
            result_box.delete(1.0, tk.END)
            idList = []
            for _ in urls:
                if _ == "" or " " in _:
                    pass
                else:
                    _ = "http://" + _
                    resourceId = queryUrlScan(_)
                    idList.append(resourceId)
                    result_box.insert(tk.END, "Scan request sent for... " + str(_) + "\n")
                    result_box.update()
                    result_box.see(tk.END)
            result_box.insert(tk.END, "Now, wait a minute. Literally.")
            for _ in range(60):
                result_box.delete(1.0, tk.END)
                result_box.insert(tk.END, str(60 - _) + " seconds to go...")
                time.sleep(1)
                result_box.update()
            result_box.delete(1.0, tk.END)
            result_box.update()
            for _ in idList:
                insertReport(_)
                report = extractReportById(_)
                result_box.insert(tk.END, str(report) + "\n")
                result_box.update()
                result_box.see(tk.END)
            result_box.configure(state="disabled")

       b1_get_report = dbutton(self, 
       text="Get the report!",
       command=get_urls
       )

       instruction.pack(side="top",
       pady=15
       )

       b1_get_report.pack(side="bottom",
       padx=20,
       pady=20
       )

       url_box.pack(side="left", 
       padx=20
       )

       result_box.pack(side="right",
       padx=20
       )