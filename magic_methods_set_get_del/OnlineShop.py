class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)


class Product:
    _id_instance = 1

    def __init__(self, name, weight, price):
        self.id = Product._id_instance
        self.name = name
        self.weight = weight
        self.price = price
        Product._id_instance += 1

    def __setattr__(self, key, value):
        if key == 'name' and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in ('weight', 'price') and type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in ('weight', 'price') and value <= 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.id}, {p.name}, {p.weight}, {p.price}")
