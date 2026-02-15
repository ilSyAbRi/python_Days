class Plant:
    def __init__(self,name,height,age):
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
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    def produce_shade(self):
        print(f"{self.name} provides {self.trunk_diameter * 2} square meters of shade")
    def show_info(self):
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")
class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    def show_nutrition(self):
        print(f"{self.name} is rich in {self.nutritional_value}")
