from collections import UserDict

class InvalidPhoneError(Exception): pass
class InvalidNameError(Exception): pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value: str):
        if not value.isalpha():
            raise InvalidNameError
        super().__init__(value)

class Phone(Field):
    def __init__(self, value: str):
        if not (value.isdigit() and len(value) == 10):
            raise InvalidPhoneError
        super().__init__(value)

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone: str):
        phone = Phone(phone)
        self.phones.append(phone)

    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def remove_phone(self, phone: str):
        phone = self.find_phone(phone)
        if phone:
            self.phones.remove(phone)
        else:
            raise ValueError(f"Phone {phone} not found")

    def edit_phone(self, old_phone: str, new_phone: str):
        new_phone = Phone(new_phone)

        for i,v in enumerate(self.phones):
            if v.value == old_phone:
                self.phones[i] = new_phone
                return True
            
        raise ValueError(f"Phone {old_phone} not found in this record.")
            
          

class AddressBook(UserDict):
    #Реалізовано метод add_record, який додає запис до self.data.
    def add_record (self, record: Record):
        self.data[record.name.value] = record

    def find (self, name: str):
        return self.data.get(name)
    
    def delete (self, name: str):
        if name in self.data:
            del self.data[name]