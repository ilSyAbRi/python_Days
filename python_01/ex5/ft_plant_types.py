class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def show_info(self):
        print(
            f"\n{self.name} (Flower): {self.height}cm, {self.age} days, "
            f"{self.color} color"
        )


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_area = self.trunk_diameter * 1.5

    def produce_shade(self):
        print(f"{self.name} provides {self.shade_area} square meters of shade")

    def show_info(self):
        print(
            f"\n{self.name} (Tree): {self.height}cm, {self.age} days, "
            f"{self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_nutrition(self):
        print(f"{self.name} is rich in {self.nutritional_value}")

    def show_info(self):
        print(
            f"\n{self.name} (Vegetable): {self.height}cm, {self.age} days, "
            f"{self.harvest_season} harvest"
        )


rose = Flower("Rose", 25, 30, "red")
lily = Flower("Lily", 20, 25, "white")

oak = Tree("Oak", 500, 1825, 50)
pine = Tree("Pine", 600, 2000, 60)

tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
carrot = Vegetable("Carrot", 30, 60, "spring", "vitamin A")

print("=== Garden Plant Types ===")

rose.show_info()
rose.bloom()
lily.show_info()
lily.bloom()

oak.show_info()
oak.produce_shade()
pine.show_info()
pine.produce_shade()

tomato.show_info()
tomato.show_nutrition()
carrot.show_info()
carrot.show_nutrition()
