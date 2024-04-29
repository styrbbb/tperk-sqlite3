import ttkbootstrap as ttk
from tkinter import *
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
#from database_sources import r_set,l1
from sqlalchemy import create_engine

conn = create_engine("sqlite:///C:\\tperk-sqlite3\\epood_tperk.db")
r_set=conn.execute("SELECT * FROM tperk")
l1=[r for r in r_set.keys()] # List of column headers 
r_set = [list(r) for r in r_set]

app = ttk.Window(themename="darkly")
app.geometry("750x400")
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



