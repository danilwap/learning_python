class Book:
    def __init__(self, title="", author="", pages=0, year=0):
        self.author = author
        self.title = title
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in ("author", "title") and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in ("pages", "year") and type(value) != int:
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)


book = Book("Python ООП", "Сергей Балакирев", 123, 2022)
