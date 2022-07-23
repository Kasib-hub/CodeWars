
def validate_pin(pin):
    # return str that have lengths of 4 and 6
    # along with them being digits

    return len(pin) in (4, 6) and pin.isdigit()
 
print(validate_pin('1234'))
print(validate_pin('a234'))
print(validate_pin('12345'))