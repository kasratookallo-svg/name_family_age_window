from datetime import date, datetime
from tkinter import *
from tkinter import messagebox
from module_product import *

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
        print(product, "Product saved successfully.")
        messagebox.showinfo("Information Saved", "Product saved successfully.")
        id_number.set(0)
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
    messagebox.showinfo("Total Price", f"Total value of all products: {total}")




window = Tk()
window.geometry("350x350")
window.title("Product Management")

# Identity Number
Label(window, text="ID num.").place(x=40, y=20)
id_number = IntVar()
Entry(window, textvariable=id_number).place(x=180, y=20)

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

window.mainloop()
