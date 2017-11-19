import Validations as validate
import datetime

MAX_VOLUME = 80000
TAX_RATE = 23

def expiration_days_to_date(days):
    today = datetime.date.today()
    timedelta = datetime.timedelta(days=days)
    expiration_date = today + timedelta
    return expiration_date

def apply_tax(price):
    return price * TAX_RATE * 0.01

def remaining_storage(current_volume):
    return MAX_VOLUME - current_volume

def build_item(name, volume, price, expiration_days, current_volume):
    item = {"name": "",
            "volume": 0,
            "price_before_tax": 0,
            "price_after_tax": 0,
            "expiry_date": None,
            "date_added": None,
            "errors": []}

    name_validation = validate.validate_name(name)
    if name_validation:
        item["errors"].append(name_validation)

    price_validation = validate.validate_price(price)
    if price_validation:
        item["errors"].append(price_validation)

    expiration_validation = validate.validate_expiration(expiration_days)
    if expiration_validation:
        item["errors"].append(expiration_validation)

    volume_validation = validate.validate_volume(volume, remaining_storage(current_volume))
    if volume_validation:
        item["errors"].append(expiration_validation)

    item["name"] = name

    item["volume"] = remaining_storage(current_volume)

    item["price_before_tax"] = price
    item["price_after_tax"] = apply_tax(price)

    item["expiry_date"] = expiration_days_to_date(expiration_days)
    item["date_added"] = datetime.date.today()

    return item

print (build_item("five", -1, -1, -1, 40000))