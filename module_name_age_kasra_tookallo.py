import re


def name_validator(name):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", name):
        raise ValueError("Invalid Name !!!")

def family_validator(family):
    if not re.match(r"^[a-zA-Z\s]{3,30}$", family):
        raise ValueError("Invalid Family !!!")

def age_validator(age):
    if not (type(age) == int and 0 < age < 150):
        raise ValueError("Invalid Age !!!")