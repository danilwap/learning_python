class RenderList:
    def __init__(self, type_list):
        if type_list in ("ul", "ol"):
            self.type_list = type_list
        else:
            self.type_list = "ul"

    def __call__(self, *args, **kwargs):
        generat_str = ''.join(map(lambda x: f"<li>{x}</li>\n", args[0]))
        res = f"<{self.type_list}>\n"+generat_str+f"</{self.type_list}>"
        return res


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList('ul')

print(render(lst))