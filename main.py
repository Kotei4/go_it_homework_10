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
        self.validate(value)
        self.value = value

    def validate(self, value):
        if type(value) != str:
            raise ValueError('Phone should be a string')
        if len(value) != 10 or not value.isdigit():
            raise ValueError('Phone should be 10 symbols')


class Record:
    def __init__(self, surname):
        self.name = Name(surname)
        self.phones = []

    def __str__(self):
        if self.phones:
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        return f"Contact name: {self.name.value}, has no phones"

    def add_phone(self, phone_number: str):
        existing_phone = self.find_phone(phone_number)
        if existing_phone is None:
            phone = Phone(phone_number)
            self.phones.append(phone)
            
    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone

    def edit_phone(self, old_phone, new_phone):
        existing_phone = self.find_phone(old_phone)
        if existing_phone is not None:
            existing_phone.validate(new_phone)
            existing_phone.value = new_phone
        else:
            raise ValueError("Phone not found")

    def remove_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if phone is not None:
            self.phones.remove(phone)


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name, None)
            
    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]
