from tkinter import *
from tkinter import filedialog

root = Tk()
root.withdraw()
root.filename = filedialog.askopenfilename(initialdir="./", title="Open Data files", filetypes=(("all files", "*.*"), ("data files", "*.csv;*.xls;*.xlsx")))
print(root.filename)


root = Tk()
root.withdraw()
root.filename = filedialog.askdirectory(initialdir="./", title="Open Data files")
print(root.filename)