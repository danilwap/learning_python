# Не готово
class StackObj:
    def __init__(self, data):
        self.__data = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if isinstance(next, StackObj) or next is None:
            self.__next = next

# Односвязный список
class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if self.last:
            self.last.next = obj

        self.last = obj
        if self.top is None:
            self.top = obj


    def pop(self):
        h = self.top
        if h is None:
            return

        while h and h.next != self.last:
            h = h.next

        if h:
            h.next = None
        last = self.last
        self.last = h
        if self.last is None:
            self.top = None

        return last


    def get_data(self):
        rsl = []
        obj = self.top

        while obj:
            rsl.append(obj.data)
            obj = obj.next

        return rsl

s = Stack()
top = StackObj("obj_1")
top2 = StackObj("obj_11")
top3 = StackObj("obj_1")
top4 = StackObj("obj_1")
s.push(top)
s.push(top2)
s.push(top)
s.push(top)
#res = s.get_data()
print()
'''   
    s.push(StackObj("obj_2"))
    s.push(StackObj("obj_3"))
    s.pop()

    res = s.get_data()
    assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"
    assert s.top == top, "атрибут top объекта класса Stack содержит неверное значение"

    h = s.top
    while h:
        res = h.data
        h = h.next

    s = Stack()
    top = StackObj("obj_1")
    s.push(top)
    s.pop()
    assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

    n = 0
    h = s.top
    while h:
        h = h.next
        n += 1

    assert n == 0, "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"

    s = Stack()
    top = StackObj("name_1")
    s.push(top)
    obj = s.pop()
    assert obj == top, "метод pop() должен возвращать удаляемый объект"'''