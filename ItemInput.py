import Validations as validate
import datetime

MAX_VOLUME = 80000
TAX_RATE = 23

def get_name():
    while(True):
        name = raw_input("Item Name: ")
        validation = validate.validate_name(name)
        if validation:
            print (validation)
        else:
            return name

def get_volume(remaining_storage):
    while (True):
        volume = input("Container volume: ")
        validation = validate.validate_volume(volume, remaining_storage)
        if validation:
            print (validation)
        else:
            return volume

def get_price():
    while (True):
        price = input("Item price: ")
        validation = validate.validate_price(price)
        if validation:
            print validation
        else:
            return price

def get_expiration():
    while (True):
        days = input("Number of days until item expires: ")
        validation = validate.validate_expiration(days)
        if validation:
            print (validation)
        else:
            return days

def expiration_days_to_date(days):
    today = datetime.date.today()
    timedelta = datetime.timedelta(days=days)
    expiration_date = today + timedelta
    return expiration_date

def apply_tax(price):
    return price * TAX_RATE * 0.01

def remaining_storage(current_volume):
    return MAX_VOLUME - current_volume


def get_item_from_user(current_volume):
    item = {"name": "",
            "volume": 0,
            "price_before_tax": 0,
            "price_after_tax": 0,
            "expiry_date": None,
            "date_added": None}

    item["name"] = get_name()

    item["volume"] = get_volume(remaining_storage(current_volume))

    price = get_price()
    item["price_before_tax"] = price
    item["price_after_tax"] = apply_tax(price)

    expiration_days = get_expiration()
    item["expiry_date"] = expiration_days_to_date(expiration_days)
    item["date_added"] = datetime.date.today()
    return item