# Define function age for birthdate

from datetime import date  # using datetime and import library


def age(birthdate):   # define birthdate
    today = date.today()   # retrieving todays date
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
