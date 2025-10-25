import re
import datetime

price = 0
quantity = 0
product_list = []

def name_validator(name):
    if re.match(r"^[a-zA-Z\s]{2,20}$",name):
        return name
    else:
        raise ValueError("Name must be a string")
def brand_validator(brand):
    if re.match(r"^[a-zA-Z\s]{2,20}$" , brand):
        return brand
    else:
        raise ValueError("Brand must be a string")
def id_validator(id_number):
    if re.match(r"^[\d\s]{3,30}$", id_number):
        return id_number
    else:
        raise ValueError("Invalid Id Number !!!")
def price_validator(price):
    if (type(price) == int):
        return price
    else:
        raise ValueError("Price must be a positive number")
def quantity_validator(quantity):
    if (type(quantity) == int):
        return quantity
    else:
        raise ValueError("Quantity must be a positive number")
def expire_validator(expire_date):
    if not re.match(r"[0-9]{4}/[0-9]{2}/[0-9]{2}", expire_date):
        raise ValueError("Expiration date must be YYYY/MM/DD.")

