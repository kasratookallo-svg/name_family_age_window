from super_market_module import *

from tkinter import *


window = Tk()
window.title("Name id price Window")
window.geometry("400x400")

Label(window, text="Id").place(x=20, y=20)
id_number = IntVar()
Entry(window).place(x=100, y=20)


Label(window, text="Name").place(x=20, y=60)
name = StringVar()
Entry(window, textvariable=name).place(x=100, y=60)


label = Label(window, text="price: ").place(x=20, y=100)
price = IntVar()
Entry(window).place(x=100, y=100)

Button(window, text="Save").place(x=100, y=200)
window.mainloop()
