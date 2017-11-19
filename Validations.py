# all validations for user input

def validate_numericality(input):
    try:
        float(input)
        return False
    except ValueError:
        return True


def validate_length(input, maxlength):
    if len(input) > maxlength:
        return True
    else:
        return False

def validate_magnitude(input, min=None, max=None):
    if not min or input < min:
        return True
    elif not max or input > max:
        return True
    else:
        return False

def validate_empty(input):
    if len(input) == 0:
        return True
    else:
        return False

# Name
def validate_name(name):
    if validate_empty(name):
        return "Name cannot be empty"
    if validate_length(name, 100):
        return "Name must be less than 100 characters"
    else:
        return False
# Any value that is less than 100 characters
# required

# Volume
def validate_volume(volume, remaining_storage):
    if validate_empty(volume):
        return "Volume cannot be empty"
    if validate_numericality(volume):
        return "Volume must be a number"
    if validate_magnitude(volume, 0, remaining_storage):
        return "Volume must be greater than 0 and less than " + str(remaining_storage)
    else:
        return False
# Numerical
# required
# above 0
# below maximum storage?

# Price
def validate_price(price):
    if validate_empty(price):
        return "Price cannot be empty"
    if validate_numericality(price):
        return "Price must be a number"
    if validate_magnitude(price, 0):
        return "Price must be greater than 0"
    else:
        return False

# Numerical
# required
# above 0

def validate_expiration(days):
    if validate_empty(days):
        return "Number of days until expiration cannot be empty"
    if validate_numericality(days):
        return "Number of days until expiration must be a number"
    if validate_magnitude(days, 0):
        return "Number of days until expiration must be greater than 0"
    else:
        return False
# Expiration days
# required
# Numerical
# above 0