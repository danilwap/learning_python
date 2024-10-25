class WordString:
    def __init__(self, string=''):
        self.__string = string

    def __len__(self):
        if not self.__string:
            return 0
        elif ' ' not in self.__string:
            return 1
        else:
            return len(self.__string.split())

    def len(self, words):
        ob = WordString(words)
        return len(ob)

    def __call__(self, indx, *args, **kwargs):
        if self.__len__() > indx:
            return self.__string.split()[indx]

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        self.__string = value


words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")

