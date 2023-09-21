from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        value = ''.join(filter(str.isdigit, value))
        if len(value) == 10:
            self.value = value
        else:
            raise ValueError


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def find_phone(self, phone):
        for p in self.phones:
            if phone == p.value:
                print(f"match found {phone} == {p.value}")
                return p.value
        return

    def add_phone(self, phone):
        print(f"before adding : {self.phones}")
        self.phones.append(Phone(phone))
        print(f"after adding : {self.phones}")

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                print(f"before removing : {self.phones}")
                self.phones.remove(p)
                print(f"after removing : {self.phones}")
                return p.value
        raise ValueError

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                self.remove_phone(old_phone)
                self.add_phone(new_phone)
                return
        raise ValueError


class AddressBook(UserDict):

    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data.update({record.name.value: record})
        return f"Sucsessfully added record:\n{record}"

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, record):
        if record in self.data:
            del self.data[record]
        else:
            return


# --------------
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
