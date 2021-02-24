import tkinter as tk
from tkinter import ttk
import requests
import bs4

root = tk.Tk()
scrwdth = root.winfo_screenwidth()
scrhgt = root.winfo_screenheight()
xLeft = int((scrwdth / 2) - (350 / 2))
yTop = int((scrhgt / 2) - (280/ 2))
strg="350x280+"+str(xLeft)+"+"+str(yTop)
root.geometry(strg)
root.title("Product Search")
root.resizable(0,0)
root.wm_iconbitmap('SearchIcon.ico')
# root.overrideredirect(1)
Labelfont=("Times New Roman", 12)
titleLabel = tk.Label(root,text="Product Search",font=("Segoe UI", 20)).place(x=80,y=10)
ProductNameLabel = tk.Label(root, text="Product Name :",font=Labelfont).place(x=10,y=55)
ProductEntry = tk.Entry(root,width=30).place(x=150,y=60)

NumOfProdLabel = tk.Label(root, text="Number of Products :",font=Labelfont).place(x=10,y=85)
NumTup=[]
intg = tk.IntVar()
NumTup = [i for i in range(10,51)]
NumEntry = ttk.Combobox(root, width=27,textvariable=intg)
NumEntry['values'] = tuple(NumTup)
NumEntry.current(0)
NumEntry.place(x=150,y=90)


SortByLabel = tk.Label(root, text="Sort By :",font=Labelfont).place(x=10,y=115)
n = tk.StringVar()
SortEntry = ttk.Combobox(root, width=27,textvariable=n)
SortEntry['values'] = ('Price: Low to High','Price: High to Low','Featured','Newest Arrivals')
SortEntry.current(2)
SortEntry.place(x=150,y=120)

PriceLabel = tk.Label(root, text="Price Range :",font=Labelfont).place(x=10,y=145)
m = tk.StringVar()
PriceEntry = ttk.Combobox(root, width=27,textvariable=m)
PriceEntry['values'] = ('No limit','Under Rs.1000','Rs.1000 - Rs.5000','Rs.5000 - Rs.10000','Rs.10000 - Rs.20000','Over Rs.20000')
PriceEntry.current(0)
PriceEntry.place(x=150,y=145)

PincodeLabel = tk.Label(root, text="Delivery Pincode :",font=Labelfont).place(x=10,y=175)
PincodeEntry = tk.Entry(root,width=30)
PincodeEntry.insert(0,'400072')
PincodeEntry.place(x=150,y=175)
SearchButton = tk.Button(root,text="Search",font=Labelfont,width=10).place(x=125,y=220)
root.mainloop()