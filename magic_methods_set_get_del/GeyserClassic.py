import time

class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slots = {(1, 'Mechanical'): None, (2, 'Aragon'): None, (3, 'Calcium'): None}

    def add_filter(self, slot_num, filter):
        key = (slot_num, filter.__class__.__name__)
        if key in self.slots.keys() and not self.slots[key]:
            self.slots[key] = filter


    def water_on(self):
        if not all(self.slots.items()):
            return False
        for i in self.slots.items():
            if 0 <= time.time() - i.date <= self.MAX_DATE_FILTER:
                continue
            else:
                return False
        else:
            return True

    def get_filters(self):
        return tuple(self.slots)

    def remove_filter(self, slot_num):
        self.slots[slot_num - 1] = {}


class Mechanical:

    def __init__(self, date):
        self.date = date

    def __getattr__(self, item):
        return False

    def __setattr__(self, key, value):
        if not self.date:
            object.__setattr__(self, key, value)

    def __repr__(self):
        return f'Класс {self.__class__.__name__}'


class Aragon:
    def __init__(self, date):
        self.date = date

    def __getattr__(self, item):
        return False

    def __setattr__(self, key, value):
        if not self.date:
            object.__setattr__(self, key, value)

    def __repr__(self):
        return f'Класс {self.__class__.__name__}'



class Calcium:
    def __init__(self, date):
        self.date = date

    def __getattr__(self, item):
        return False

    def __setattr__(self, key, value):
        if not self.date:
            object.__setattr__(self, key, value)

    def __repr__(self):
        return f'Класс {self.__class__.__name__}'


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on() # False
print(my_water.get_filters())


