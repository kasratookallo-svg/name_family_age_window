import re
from datetime import date

product_list = []


def name_validator(name):
    if re.match(r"^[a-zA-Z\s]{2,20}$", name):
        return name
    else:
        raise ValueError("Name must be a string")


def brand_validator(brand):
    if re.match(r"^[a-zA-Z\s]{2,20}$", brand):
        return brand
    else:
        raise ValueError("Brand must be a string")


def id_validator(id_number):
    if type(id_number) == int and id_number > 0:
        return id_number
    else:
        raise ValueError("Invalid Id Number !!!")


def price_validator(price):
    if type(price) == float and price > 0:
        return price
    else:
        raise ValueError("Price must be a positive number")


def quantity_validator(quantity):
    if type(quantity) == int and quantity > 0:
        return quantity
    else:
        raise ValueError("Quantity must be a positive number")


def expire_validator(expire_date):
    if type(expire_date) != date and expire_date >= date.today():
        raise ValueError("Expiration date must be YYYY/MM/DD.")
