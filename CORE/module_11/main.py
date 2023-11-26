from collections import UserDict
from datetime import date, datetime, timedelta


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
    pass


class Birthday(Field):
    def __init__(self, birthday):
        if birthday is None:
            self.birthday = birthday
        else:
            birthday = "".join(filter(str.isdigit, birthday))
            if len(birthday) == 6:
                dt_bd = datetime.strptime(birthday, "%d%m%y")
                self.birthday = dt_bd
            elif len(birthday) == 8:
                dt_bd = datetime.strptime(birthday, "%d%m%Y")
                self.birthday = dt_bd
            else:
                raise ValueError("Date should be in format dd/mm/yy or dd/mm/yyyy")


class Phone(Field):
    def __init__(self, value):
        value = "".join(filter(str.isdigit, value))
        if len(value) == 10:
            self.value = value
        else:
            raise ValueError


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def find_phone(self, phone):
        for p in self.phones:
            if phone == p.value:
                return p
        return

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

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

    def days_to_birthday(self):
        if self.birthday.birthday is None:
            return None
        today_date = datetime.now()
        current_year = today_date.year
        birthday = self.birthday.birthday
        next_birthday = birthday.replace(year=current_year)

        if next_birthday < today_date:
            next_birthday = birthday.replace(year=current_year + 1)
        days_to_bd = next_birthday - today_date

        return days_to_bd.days


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
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John", "26/09/2023")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # creating big list
    for someone in range(1, 14):
        book.add_record(Record(f"Name num{someone}", f"{someone + 10}/09/2023"))

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    print(jane_record.days_to_birthday())
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)
        pass

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    # print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    # print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

    # Тест пагінації
    for i in book.iterator():
        print(i)
        input()
