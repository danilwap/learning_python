class Ingredient:
    def __init__(self, name: str, volume: float, measure: str):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {str(self.volume)}, {self.measure}"


class Recipe:
    def __init__(self, *args):
        self.ings = []
        if args:
            self.ings.extend(args)

    def add_ingredient(self, ing):
        self.ings.append(ing)

    def remove_ingredient(self, ing):
        if ing in self.ings:
            self.ings.remove(ing)

    def get_ingredients(self):
        return tuple(self.ings)

    def __len__(self):
        return len(self.ings)


recipe = Recipe()
ing1 = Ingredient("Соль", 1, "столовая ложка")
recipe.add_ingredient(ing1)
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
recipe.remove_ingredient(ing1)

n = len(recipe) # n = 3

