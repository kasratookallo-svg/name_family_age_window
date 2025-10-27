from datetime import date, datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


#todo from persiantools.digits import to_word

from module_product import *
from tkinter import ttk

product_list = []

def save():
    try:
        id_validator(id_number.get())
        name_validator(name.get())
        brand_validator(brand.get())
        quantity_validator(quantity.get())
        price_validator(price.get())

        # تبدیل تاریخ از رشته به تاریخ
        expire_date = datetime.strptime(expiration_date.get(), "%Y-%m-%d").date()
        expire_validator(expire_date)

        product = {
            "id_number": id_number.get(),
            "name": name.get(),
            "brand": brand.get(),
            "quantity": quantity.get(),
            "price": price.get(),
            "expire_date": expire_date}

        product_list.append(product)
        table.insert("", END, values = tuple(product.values()))
        messagebox.showinfo("Information Saved", "Product saved successfully.")
        id_number.set(len(product_list)+1)
        name.set("")
        brand.set("")
        quantity.set(0)
        price.set(0)
        expiration_date.set(str(date.today()))
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong : {e}")


# total_price action
def total_price():
    if not product_list:
        messagebox.showerror("No product", "There is no products saved.")
        return

    total = 0
    for product in product_list:
        total = total + product['quantity'] * product['price']
    messagebox.showinfo("Total Price", f"Total value of all products: {total}")  #todo{to_word(total)}




window = Tk()
window.geometry("850x350")
window.title("Product Management")

# Identity Number
Label(window, text="ID num.").place(x=40, y=20)
id_number = IntVar()
Entry(window, textvariable=id_number, state="readonly").place(x=180, y=20)

# Name
Label(window, text="Name").place(x=40, y=60)
name = StringVar()
Entry(window, textvariable=name).place(x=180, y=60)

# Brand
Label(window, text="Brand").place(x=40, y=100)
brand = StringVar()
Entry(window, textvariable=brand).place(x=180, y=100)

# Quantity
Label(window, text="Quantity").place(x=40, y=140)
quantity = IntVar()
Entry(window, textvariable=quantity).place(x=180, y=140)

# Price
Label(window, text="Price").place(x=40, y=180)
price = DoubleVar()
Entry(window, textvariable=price).place(x=180, y=180)

# Expire date
Label(window, text="Expire date\n(yyyy/mm/dd)").place(x=40, y=220)
expiration_date = StringVar()
Entry(window, textvariable=expiration_date).place(x=180, y=220)

# Buttons
Button(window, text="Submit", command=save).place(x=40, y=300, width=100)
Button(window, text="Total", command=total_price).place(x=200, y=300, width=100)

table = ttk.Treeview(window , columns=(1,2,3,4,5,6),height = 14,  show="headings")
table.heading(1, text="ID")
table.heading(2, text="Name")
table.heading(3, text="Brand")
table.heading(4, text="Quantity")
table.heading(5, text="Price")
table.heading(6, text="Expiration date")

table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=30)
table.column(5, width=30)
table.column(6, width=100)


table.place(x=400, y=20)

window.mainloop()
