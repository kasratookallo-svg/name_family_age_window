import re


def name_validator(name):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", name):
        raise ValueError("Invalid Name !!!")

def id_validator(id_number):
    if not re.match(r"^[\d\s]{3,30}$", id_number):
        raise ValueError("Invalid Id Number !!!")

def price_validator(price):
    if not (type(price) == int and 0 < price < 150):
        raise ValueError("Invalid price !!!")