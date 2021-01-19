import tkinter as tk
import tkinter.scrolledtext as stxt

from modules.gui.darkMotive import dframe, dbutton, dlabel, dpage
from modules.local.databaseOperations import searchDatabase

class historyPage(dpage):
   def __init__(self, *args, **kwargs):
       dpage.__init__(self, *args, **kwargs)

       instrucion = dlabel(self, 
       text='Insert domain to search for and click on "Search!" button.')

       result_box = stxt.ScrolledText(self, 
       fg="white", 
       bg="gray15",
       insertofftime=0,
       width=100,
       height=40,
       wrap="none",
       insertbackground="white",
       state="disabled"
       )

       searchPhrase = tk.Entry(self,
       width=64,
       bg="gray15",
       fg="white"
       ) 

       def seekAndDestroy():
           keyword = searchPhrase.get()
           forbidden_dictionary = ["", "DROP", "*", "NULL", " ", "-", "'", '"']
           if keyword in forbidden_dictionary:
                result_box.configure(state="normal")
                result_box.delete(1.0, tk.END)
                result_box.insert(tk.END, "Really?")
                result_box.configure(state="disabled")
           else:
                result = searchDatabase(keyword)
                result_box.configure(state="normal")
                result_box.delete(1.0, tk.END)
                for _ in result:
                    if _ in result_box.get(1.0, tk.END):
                        pass
                    else:
                        _ = _ + "\n"
                        result_box.configure(state="normal")
                        result_box.insert(tk.END, _)
                        result_box.configure(state="disabled")


       b1_search = dbutton(self,
       text="Search!",
       command=seekAndDestroy
       )

       instrucion.pack(side="top", pady=(10, 0))
       searchPhrase.pack(side="top", pady=(10, 0))
       b1_search.pack(side="top", pady=(10, 0))
       result_box.pack(side="top", pady=(10, 0))