from super_market_module import *
import tkinter
from tkinter import *


window = Tk()
window.title("Name id price Window")
window.geometry("600x400")

Label = Label(window, textvariable="name: ").place(x=20, y=20)
name = StringVar()
Entry = Entry(window, textvariable=name).place(x=100, y=40)

label = Label(window, textvariable="ID: ").place(x=20, y=60)
entry = Entry(window).place(relx=100, rely=60)
id_number = IntVar()

label = Label(window, textvariable="price: ").place(x=20, y=100)
price = IntVar()
entry = Entry(window).place(x=100, y=100)

button = Button(window).place(x=100, y=200)
window.mainloop()
