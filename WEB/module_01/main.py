import addressbook


def input_error(func):
    def wrapper(*args: str):
        try:
            result = func(*args)
        except KeyError:
            result = "Wrong input!"
        except ValueError:
            result = "Missing contact information"
        except IndexError:
            result = "catch IndexError"
        except TypeError:
            result = "catch TypeError"
        except Exception as e:
            result = f"an unexpected error occurred: {e}"
        return result
    return wrapper


@input_error
def hello_handler():
    return "How can I help you?"


@input_error
def add_handler(name):
    '''usage: 

        add [firstname] [surname]
    or: add [name]

    names should not include numbers!!'''

    new_user = addressbook.Record(name)
    return abook.add_record(new_user)


@input_error
def change_handler(arg: list) -> str:
    '''usage: 
        change [name] [old phone] [new phone]

    phones should be either 7 or 10 char long'''
    name, old_phone, new_phone = arg
    name = name.lower()
    if abook.get(name, None).phones:
        abook.get(name, None).edit_phone(old_phone, new_phone)
        return f"Changed {name} : {old_phone} to {new_phone}"
    else:
        return "Contact does not exist"
    

@input_error
def change_birthday(arg):
    '''usage: 
        birthday [name] [new birthday in format xx/xx/xxxx]'''
    name, birthday = arg
    if abook.get(name, None):
        abook.get(name, None).edit_birthday(birthday)
        return f"Changed birthday to {birthday}"
    else:
        return "Contact does not exist"


@input_error
def change_birthday(arg):
    '''usage: 
        birthday [name] [new birthday in format xx/xx/xxxx]'''
    name, birthday = arg
    if abook.get(name, None):
        abook.get(name, None).edit_birthday(birthday)
        return f"Changed birthday to {birthday}"
    else:
        return "Contact does not exist"


@input_error
def add_phone_handler(arg: list):
    '''usage:
        phone [name] [phone]
    phones should be either 7 or 10 char long'''
    name, phone = arg
    result = abook.get(name.lower()).add_phone(phone)
    abook.save()
    return result


@input_error
def show_all_handler():
    '''usage:
        show all'''
    out = "Contacts found:\n"
    name = abook.find_all("")
    for n in name:
        out += f"{n}\n"
    if len(name) > 0:
        return out
    else:
        return "Contact list is empty"


@input_error
def search_handler(input):
    '''usage:
        search [any str or int]'''
    if len(input) == 1:
        input = input[0]
        out = "Contacts found:\n"
        results = abook.find_all(input)
        for res in results:
            out += f"{res}\n"
        if len(results) > 0:
            return out
        else:
            return "Contact list is empty"
    else:
        raise ValueError("Wrong search input")


@input_error
def find_handler(input: list):
    '''usage:
        find [name]
    or  find [first name] [second name]'''
    if len(input) == 1:
        input = input[0]
        return abook.find(input.lower())
    elif len(input) == 2:
        name, surname = input.lower()
        return abook.find(f"{name}, {surname}")
    else:
        raise ValueError("Wrong find input")


@input_error
def exit_handler() -> None:
    abook.save()
    return "closing"


def main():
    COMMANDS_NO_ARG = {"hello": hello_handler, "show all": show_all_handler,
                       "good bye": exit_handler, "close": exit_handler, "exit": exit_handler}
    COMMANDS_ARG = {"add": add_handler,
                    "change": change_handler, "birthday":change_birthday, "phone": add_phone_handler, "search": search_handler, "find": find_handler}
    out = True
    print("Hello User!")
    while out != "closing":
        user_input = input("::> ")

        try:
            command, *args = user_input.split()
            out = COMMANDS_ARG[command.lower()](args)
        except KeyError:
            command = user_input
            if command not in COMMANDS_NO_ARG:
                out = "Unknown command"
            else:
                out = COMMANDS_NO_ARG[command.lower()]()

        print(out)


# main loop
if __name__ == '__main__':
    abook = addressbook.AddressBook()
    main()
