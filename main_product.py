import tkinter
from math import *
from tkinter import *
from tkinter import messagebox
from module_product import *

majmoo = 0
product_list = []


def save():
# _____________________________________________________________________________________________________________________________
    try:
        # todo Validators does'nt work properly
        # id_validator(id_number.get())
        # price_validator(price.get())
        # name_validator(name.get())
        # brand_validator(brand.get())
        # quantity_validator(quantity.get())
        # expire_validator(expire_date.get())
# _________________________________________________________________________________________________________________________________________

        product = {"name": name.get(), "brand": brand.get(), "quantity": quantity.get(), "price": price.get(),
                   "id_number": id_number.get()}
        product_list.append(product)
        print(product, "Product saved successfully.")
        messagebox.showinfo("Information Saved", "Product saved successfully.")
        id_number.set("")
        name.set("")
        brand.set("")
        quantity.set(0)
        price.set(0)
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong : {e}")


print(product_list)
# _________________________________________________________________________________________________
def total_price():
    for product in product_list:
        majmoo = price.get() * quantity.get()
# majmoo = majmoo + product['quantity'] * product['price']
    print("total price is ", majmoo)
# _________________________________________________________________________________________________
window = Tk()
window.geometry("600x400")
window.title("Product Management")

# Name
Label(window, text="Name").place(x=40, y=20)
name = StringVar()
Entry(window, textvariable=name).place(x=180, y=20)
# Brand
Label(window, text="Brand").place(x=40, y=60)
brand = StringVar()
Entry(window, textvariable=brand).place(x=180, y=60)
# Price
Label(window, text="Price").place(x=40, y=100)
price = DoubleVar()
Entry(window, textvariable=price).place(x=180, y=100)
# Quantity
Label(window, text="Quantity").place(x=40, y=140)
quantity = IntVar()
Entry(window, textvariable=quantity).place(x=180, y=140)
# Identity Number
Label(window, text="ID num.").place(x=40, y=180)
id_number = StringVar()
Entry(window, textvariable=id_number).place(x=180, y=180)
# Expire date
Label(window, text="Expire date.(yyyy/mm/dd)").place(x=40, y=220)
expiration_date = StringVar()
Entry(window, textvariable=expiration_date).place(x=180, y=220)
Button(window, text="Submit", command=save).place(x=180, y=300, width=70, height=60)
Button(window, text="Total", command=total_price).place(x=280, y=300, width=70, height=60)

window.mainloop()