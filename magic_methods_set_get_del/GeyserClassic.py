class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slots = [{}, {}, {}]

    def add_filter(self, slot_num, filter):


class Mechanical:
    def __init__(self, date):
        self.date = date

    def __getattr__(self, item):
        return False

    def __setattr__(self, key, value):
        if not self.date:
            object.__setattr__(self, key, value)


class Aragon:
    def __init__(self, date):
        self.date = date

    def __getattr__(self, item):
        return False

    def __setattr__(self, key, value):
        if not self.date:
            object.__setattr__(self, key, value)



class Calcium:
    def __init__(self, date):
        self.date = date

    def __getattr__(self, item):
        return False

    def __setattr__(self, key, value):
        if not self.date:
            object.__setattr__(self, key, value)


mc = Mechanical(123)