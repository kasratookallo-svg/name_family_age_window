import re
from main import name, brand, id_number, price, quantity
product_list = []

def name_validator():
    if not re.match(r"^[a-zA-Z\s]{2,20}$",name):
        raise ValueError("Name must be a string")
def brand_validator():
    if not re.match(r"^[a-zA-Z\s]{2,20}$" , brand):
        raise ValueError("Brand must be a string")
def id_validator(id_number):
    if not re.match(r"^[\d\s]{10}$", id_number):
        raise ValueError("Id Number must be a ten digit number !!!")
def price_validator():
    if not 0<price:
        raise ValueError("Price must be a positive number")

def total_price():
    total = price.get() * quantity.get()