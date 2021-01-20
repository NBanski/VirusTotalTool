import tkinter as tk
import tkinter.scrolledtext as stxt

from modules.gui.darkMotive import dframe, dbutton, dlabel, dpage
from modules.local.databaseOperations import insertReport, extractReportByUrl

class reportsPage(dpage):
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
       state="disabled"
       )

       instruction = dlabel(self, 
       text="""Insert URLs for which you want reports into the left box. Result will appear in the right box.
Acceptable format is <domain name>.<extension>. Do not use any protocol prefixes.""",
       justify="left"
       )

       def getUrls():
        urls = url_box.get("1.0", "end-1c").split("\n")
        result_box.configure(state="normal")
        result_box.delete(1.0, tk.END)
        unfound = []
        for _ in urls:
            if _ == "" or " " in _:
                pass
            else:
                domain = _
                _ = "http://" + _
                insertReport(_)
                report = extractReportByUrl(_) + "\n"
                result_box.insert(tk.END, report)
                result_box.update()
                result_box.see(tk.END)
                if "not found" in report:
                    unfound.append(domain)
                else:
                    pass
        if unfound:
            result_box.insert(tk.END, "\nDomains that were not found:\n")
            for _ in unfound:
                result_box.insert(tk.END, (_ + "\n"))
        else:
            pass
        result_box.configure(state="disabled")


       b1_get_report = dbutton(self, 
       text="Get the report!",
       command=getUrls
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