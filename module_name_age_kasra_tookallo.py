import re


def name_validator(name):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", name):
        raise ValueError("Invalid Name !!!")

def id_validator(id_number):
    if not re.match(r"^[\d\s]{3,30}$", family):
        raise ValueError("Invalid Family !!!")

def age_validator(age):
    if not (type(age) == int and 0 < age < 150):
        raise ValueError("Invalid Age !!!")