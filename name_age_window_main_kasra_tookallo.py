from module_name_age_kasra_tookallo import *
import tkinter
from tkinter import *


try:
    name = input("Enter your name: ")
    name = name_validator(name)
    family = input("Enter your family: ")
    family = family_validator(family)
    age = int(input("Enter your age: "))
    age_validator(age)
except:
    print("Invalid data !!!")

window = Tk()
window.title("Name family Age Window")
window.geometry("600x400")

label = Label(window, text="I: ").place(relx=20, rely=20)
name =
entry = Entry(window).place(relx=100, rely=40)

label = Label(window, text="family: ").place(relx=20, rely=60)
entry = Entry(window).place(relx=100, rely=60)

label = Label(window, text="age: ").place(relx=20, rely=100)
entry = Entry(window).place(relx=100, rely=100)
