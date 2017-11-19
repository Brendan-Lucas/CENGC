import Validations as validate
import QueryScript

def get_name():
    while(True):
        name = raw_input("Item Name: ")
        validation = validate.validate_name(name)
        if validation:
            print(validation)
        else:
            return name

def get_volume(remaining_storage):
    while (True):
        volume = input("Container volume: ")
        validation = validate.validate_volume(volume, remaining_storage)
        if validation:
            print(validation)
        else:
            return volume

def get_price():
    while (True):
        price = input("Item price: ")
        validation = validate.validate_price(price)
        if validation:
            print(validation)
        else:
            return price

def get_expiration():
    while (True):
        days = input("Number of days until item expires: ")
        validation = validate.validate_expiration(days)
        if validation:
            print(validation)
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

def do(action):
    if action == "1":
        QueryScript.allItems()
    elif action == "2":
        item_name = raw_input("Item name: ")
        QueryScript.itemsWithName(item_name)
    elif action == "3":
        #total cost
        print("total cost is not yet implemented")
    elif action == "4":
        name = get_name()
        price = get_price()
        remaining_storage = QueryScript.remainingStorage()
        volume = get_volume(remaining_storage)
        expiry_days = get_expiration()
        QueryScript.AddItem(name, volume, price, expiry_days)
    elif action == "5":
        while(True):
            fieldnum = raw_input("What field would you like to search by?(1.Name, 2.volume, 3.ExpirationDate, 4.ID): ")
            if fieldnum == "1":
                field = "Name"
            elif fieldnum == "2":
                field = "volume"
            elif fieldnum == "3":
                field = "ExpirationDate"
            elif fieldnum == "4":
                field = "ID"
            else:
                print("That is not a valid input")
        value = raw_input("Item " + field + " for removal: ")
        QueryScript.remove_item(value, field)
    elif action == "6":
        QueryScript.storageStatus()
    elif action == "7":
        id = raw_input("Item ID to get expiry date of: ")
        QueryScript.daysToExpire(id)

def run():
    while(True):
        action = raw_input("What would you like to do?\n 1. List all items\n 2. Search items by name\n 3. Total Cost\n 4. Add Item\n 5. Remove an Item\n 6. Get the storage status\n 7. Get the expiry status of an item\n 8. Test SMS\n 9. quit")
        if action == "9":
            break
        elif action in ["1", "2", "3", "4", "5", "6", "8"]:
            do(action)

run()