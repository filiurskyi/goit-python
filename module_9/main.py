

def input_error(func):
    def wrapper(*args: str):
        try:
            result = func(*args)
        except KeyError:
            result = "Wrong input!"
        except ValueError:
            result = "missing contact information"
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
def add_handler(arg):
    name, phone = arg
    if not contacts.get(name, None):
        contacts.update({name: phone})
        return f"Added {name} : {phone}"
    else:
        return "Contact already in phonebook"


@input_error
def change_handler(arg):
    name, phone = arg
    if contacts.get(name, None):
        contacts.update({name: phone})
        return f"Changed {name} : {phone}"
    else:
        return "Contact does not exist"


# @input_error
def phone_handler(arg):
    name = arg[0]
    return contacts.get(name, "No such contact")


@input_error
def show_all_handler():
    if len(contacts) == 0:

        return "Your contact list is empty"
    return '\n'.join([f'{name} : {phone}' for name, phone in contacts.items()])


@input_error
def exit_handler():
    return "closing"



def main():
    COMMANDS_NO_ARG = {"hello": hello_handler, "show all": show_all_handler,
                       "good bye": exit_handler, "close": exit_handler, "exit": exit_handler}
    COMMANDS_ARG = {"add": add_handler,
                    "change": change_handler, "phone": phone_handler}
    out = True
    print("Hello User!")
    while out != "closing":
        user_input = input("::> ")

        try:
            command, *args = user_input.split()
            out = COMMANDS_ARG[command.lower()](args)
        except:
            command = user_input
            out = COMMANDS_NO_ARG[command.lower()]()

        print(out)


# main loop
if __name__ == '__main__':
    contacts = {}
    main()
