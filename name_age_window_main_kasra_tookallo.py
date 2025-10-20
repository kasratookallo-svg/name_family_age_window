from module_name_age_kasra_tookallo import *
import tkinter
from tkinter import *


try:
    name = input("Enter your name: ")
    name = name_validator(name)
    id= int(input("Enter your family: "))
    id = id_validator(id_number)
    price = float(input("Enter your age: "))
    price_validator(price)
except:
    print("Invalid data !!!")

window = Tk()
window.title("Name id price Window")
window.geometry("600x400")

label = Label(window, text="name: ").place(relx=20, rely=20)
name =
entry = Entry(window).place(relx=100, rely=40)

label = Label(window, text="ID: ").place(relx=20, rely=60)
entry = Entry(window).place(relx=100, rely=60)

label = Label(window, text="price: ").place(relx=20, rely=100)
entry = Entry(window).place(relx=100, rely=100)
