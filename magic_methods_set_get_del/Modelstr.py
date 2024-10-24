class Model:
    def __init__(self):
        self.req = {}

    def query(self, **kwargs):
        self.req = kwargs

    def __str__(self):
        if self.req:
            return "Model: " + ", ".join(f"{str(x[0]) + ' = ' + str(x[1])}" for x in self.req.items())
        else:
            return "Model"

