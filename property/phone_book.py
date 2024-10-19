class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio

class PhoneBook():
    def __init__(self):
        self.phone_list = []
    def add_phone(self, phone):
        self.phone_list.append(phone)

    def remove_phone(self, indx):
        if len(self.phone_list) - 1 >= indx:
            self.phone_list.pop(indx)

    def get_phone_list(self):
        return self.phone_list



p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)