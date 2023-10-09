from collections import UserDict
from datetime import datetime
from random import randint
import os
import pickle


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'adressbook.bin')


class Field:
    def __init__(self, value):
        self.__value = value
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if len(value) == 2:
            first_name, second_name = value
            if not first_name.isalpha():
                raise ValueError("First name may not have numbers")
            elif not second_name.isalpha():
                raise ValueError("Second name may not have numbers")
            else:
                new_user = f"{first_name.lower()}, {second_name.lower()}"
                self.value = new_user
        elif len(value) == 1:
            value = value[0]
            if not value.isalpha():
                raise ValueError("Second name may not have numbers")
            else:
                new_user = value
                self.value = new_user.lower()
        else:
            raise ValueError("Wrong name input")

    def __str__(self):
        return self.value.title()


class Birthday(Field):
    def __init__(self, birthday):
        if birthday is None:
            self.birthday = birthday
        else:
            birthday = ''.join(filter(str.isdigit, birthday))
            if len(birthday) == 6:
                dt_bd = datetime.strptime(birthday, "%d%m%y")
                self.birthday = dt_bd
            elif len(birthday) == 8:
                dt_bd = datetime.strptime(birthday, "%d%m%Y")
                self.birthday = dt_bd
            else:
                raise ValueError(
                    "Date should be in format dd/mm/yy or dd/mm/yyyy")

    def __str__(self):
        if self.birthday is None:
            return "\"\""
        else:
            return str(self.birthday.date())


class Phone(Field):
    def __init__(self, value: str) -> None:
        value = ''.join(filter(str.isdigit, value))
        if len(value) == 10:
            self.value = value
        elif len(value) == 8:
            self.value = "80" + value
        else:
            raise ValueError

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name}\nBirthday: {self.birthday}\nPhones: {'; '.join(p.value for p in self.phones)}"

    def find_phone(self, phone):
        for p in self.phones:
            if phone == p.value:
                return p
        return

    def add_phone(self, phone: str) -> str:
        new_phone = Phone(phone)
        self.phones.append(new_phone)
        return f"Added {new_phone} to {self.name}"

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return self
        raise ValueError

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                self.remove_phone(old_phone)
                self.add_phone(new_phone)
                return self
        raise ValueError
    
    def edit_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        if self.birthday.birthday is None:
            return None
        today_date = datetime.now()
        current_year = today_date.year
        birthday = self.birthday.birthday
        next_birthday = birthday.replace(year=current_year)

        if next_birthday < today_date:
            next_birthday = birthday.replace(year=current_year+1)
        days_to_bd = next_birthday - today_date

        return days_to_bd.days


class AddressBook(UserDict):

    def __init__(self):
        try:
            with open(filename, "rb") as f:
                fr = f.read()
                if fr:
                    data = pickle.loads(fr)
                    self.data = data
                else:
                    self.data = {}
        except FileNotFoundError:
            self.data = {}

    def __repr__(self) -> str:
        out = ""
        for name in self:
            d = self.data.get(name, None)
            out += f"{d}\n"
        return out

    def add_record(self, record):
        self.data.update({record.name.value: record})
        self.save()
        return f"Sucsessfully added record:\n{record}"

    def find(self, name: str) -> Record:
        return self.data.get(name, None)

    def find_all(self, input: str) -> list:
        input = input.lower()
        find_result = []
        for contact in self.data.values():
            if input in str(contact.name).lower() and contact.name not in find_result:
                find_result.append(contact.name)
            for single_phone in contact.phones:
                if input in str(single_phone) and contact.name not in find_result:
                    find_result.append(contact.name)
        return find_result

    def delete(self, record):
        if record in self.data:
            del self.data[record]
        else:
            return

    def save(self):
        with open(filename, "wb") as f:
            pickle.dump(self.data, f)

    def iterator(self, n=5):
        counter = 0
        output = {}
        for key, value in self.data.items():
            counter += 1
            # print(key)
            # print(f"IF {counter} == {len(self.data)}")
            if counter % n or counter == 0 or counter == len(self.data):
                output.update({key: value})
                if counter == len(self.data):
                    yield output
            else:
                output.update({key: value})
                yield output
                output = {}


if __name__ == "__main__":
    book = AddressBook()
    print(book)

    # john_record = Record("John", "26/09/2023")
    # john_record.add_phone("1234567890")
    # john_record.add_phone("5555555555")
    # book.add_record(john_record)
    # john = book.find("John")
    # john.edit_phone("1234567890", "1112223333")

    for someone in range(1, 14):

        if randint(1111111111, 9999999999) % 2:
            rand_user = Record(
                f"Name nr. {someone}", f"{someone + 10}/09/2023")
        else:
            rand_user = Record(f"Name nr. {someone}")
            rand_user.add_phone(str(randint(1111111111, 9999999999)))
        rand_user.add_phone(str(randint(1111111111, 9999999999)))

        book.add_record(rand_user)

    # jane_record = Record("Jane")
    # jane_record.add_phone("9876543210")
    # print(jane_record.days_to_birthday())
    # book.add_record(jane_record)
    # found_phone = john.find_phone("5555555555")
    # book.delete("Jane")

    # for name, record in book.data.items():
    #     print(record)
    #     pass

    # for i in book.iterator():
    #     print(i)
    #     input()

    # book.find_all("name")
