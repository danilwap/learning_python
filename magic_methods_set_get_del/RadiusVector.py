from math import sqrt


class RadiusVector:
    def __init__(self, *args):
        self.coords = {}
        if len(args) == 1:
            for i in range(args[0]):
                self.coords[i] = 0
        else:
            for i in range(len(args)):
                self.coords[i] = args[i]

    def set_coords(self, *args):
        indx = len(self.coords) if len(self.coords) <= len(args) else len(args)

        for i in range(indx):
            self.coords[i] = args[i]

    def get_coords(self):
        return tuple(self.coords.values())

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return sqrt(sum(map(lambda x: x ** 2, self.coords.values())))


