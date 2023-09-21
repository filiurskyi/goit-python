def add_phone(input):
    phone = ''.join(filter(str.isdigit, input))
    print(f"filtered phone = {phone}")
    if len(phone) == 10:
        print(f"phone {phone} is 10 len")
    elif len(phone) == 8:
        print(f"phone {phone} is 8 len")
    else:
        print(f"phone {phone} is wrong")

add_phone("1235489765")
add_phone("123548976s")
add_phone("123dfw976s")
add_phone("8 098 81 14 33")