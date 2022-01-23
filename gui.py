from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import requests
from bs4 import BeautifulSoup as bs

root = Tk()
var = StringVar()
var.set("Very simple webscraper")
label = Label(root, textvariable=var)
label.grid(column=0, row=0)
Lab1 = Label(root, text="Enter website link")
Lab1.grid(column=0, row=1)
Ent1 = tk.Entry(root)
Ent1.grid(column=1, row=1)
Lab2 = Label(root, text="Enter the class id")
Lab2.grid(column=0,row=2)
Ent2 = tk.Entry(root)
Ent2.grid(column=1, row=2)
def execute():
    messagebox.showwarning("lol", "you clicked the execute button!")
    site = Ent1.get()
    clas = Ent2.get()
    Get = requests.get(site)
    # print(Get.content)
    soup = bs(Get.content, "html.parser")
    # get = soup.findAll('div')
    # print(get)
    elements = soup.find_all("div", class_=clas)
    for elements in elements:
        print(elements, end="\n" * 2)
        Lab3 = Label(root, text=elements)
        Lab3.grid(column=0, row=4)
button = ttk.Button(text="Execute", command=execute)
button.grid(column=0, row=3)
but2 = ttk.Button(text="Quit", command=root.destroy)
but2.grid(column=1, row=3)
root.mainloop()
