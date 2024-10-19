# Решающее дерево
class TreeObj:
    def __init__(self, indx, value=None):
        self.check_index(indx)
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @classmethod
    def check_index(cls, indx):
        if not isinstance(indx, int):
            raise "Неверный формат indx"

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, obj):
        self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj):
        self.__right = obj


class DecisionTree:

    @classmethod
    def predict(cls, root, x):
        obj = root
        while obj:
            obj_next = cls.get_next(obj, x)
            if obj_next == None:
                break
            obj = obj_next

        return obj.value



    @classmethod
    def get_next(cls, obj, x):
        if x[obj.indx] == 1:
            return obj.left
        else:
            return obj.right

    @classmethod
    def add_obj(cls, obj: TreeObj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj


