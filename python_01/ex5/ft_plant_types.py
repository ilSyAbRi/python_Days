class Plant:
    """Base class for a plant with name, height, and age."""
    def __init__(self, name, height, age):
        """Initialize plant with name, height (cm), and age (days)."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """A flowering plant with a color that can bloom."""
    def __init__(self, name, height, age, color):
        """Initialize flower with color in addition to base attributes."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Print that the flower is blooming."""
        print(f"{self.name} is blooming beautifully!")

    def show_info(self):
        """Print flower details including color."""
        print(
            f"\n{self.name} (Flower): {self.height}cm, {self.age} days, "
            f"{self.color} color"
        )


class Tree(Plant):
    """A tree with trunk diameter and shade area."""
    def __init__(self, name, height, age, trunk_diameter):
        """Initialize tree with trunk diameter and calculate shade area."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_area = self.trunk_diameter * 1.5

    def produce_shade(self):
        """Print the amount of shade the tree provides."""
        print(f"{self.name} provides {self.shade_area} square meters of shade")

    def show_info(self):
        """Print tree details including trunk diameter."""
        print(
            f"\n{self.name} (Tree): {self.height}cm, {self.age} days, "
            f"{self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    """A vegetable plant with harvest season and nutritional value."""
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """Initialize vegetable with harvest season and nutrition info."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_nutrition(self):
        """Print the nutritional value of the vegetable."""
        print(f"{self.name} is rich in {self.nutritional_value}")

    def show_info(self):
        """Print vegetable details including harvest season."""
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
