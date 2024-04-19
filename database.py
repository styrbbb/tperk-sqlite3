import ttkbootstrap as ttk
from tkinter import *
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from database_sources import r_set,l1

app = ttk.Window(themename="darkly")
app.geometry("750x500")
colors = app.style.colors


dt = Tableview(
    master=app,
    paginated=True,
    searchable=True,
    bootstyle=PRIMARY,
    pagesize=10,
    height=10,
    coldata=l1,
    rowdata=r_set,
    stripecolor=(colors.dark, None),
)

dt.grid(row=0, column=0, padx=5, pady=5) 
dt.autofit_columns()

dt.build_table_data(l1,r_set)
dt.load_table_data()
dt.autofit_columns()
dt.autoalign_columns()

app.mainloop()



