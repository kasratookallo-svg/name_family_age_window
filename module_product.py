import re
import datetime

price = 0
quantity = 0
product_list = []

def name_validator(name):
    if not re.match(r"^[a-zA-Z\s]{2,20}$",name):
        raise ValueError("Name must be a string")
def brand_validator(brand):
    if not re.match(r"^[a-zA-Z\s]{2,20}$" , brand):
        raise ValueError("Brand must be a string")
def id_validator(id_number):
    if not re.match(r"^[\d\s]{3,30}$", id_number):
        raise ValueError("Invalid Id Number !!!")
def price_validator(price):
    if not (type(price) == int):
        raise ValueError("Price must be a positive number")
def quantity_validator(quantity):
    if not (type(quantity) == int):
        raise ValueError("Quantity must be a positive number")
def expire_validator(expire_date):
    if not ( expire_date.get() > datetime.datetime.today().date() ):
        raise ValueError("Expiration date must be later than today.")

