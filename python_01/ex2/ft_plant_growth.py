class Plant:
    """A plant with name, height, and age."""
    def __init__(self, name, height, age):
        """Initialize plant with name, height (cm), and age (days)."""
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        """Increase the plant's height by 1 cm."""
        self.height += 1

    def grow_older(self):
        """Increase the plant's age by 1 day."""
        self.age += 1

    def get_info(self):
        """Print the plant's name, height, and age."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("rose", 25, 30)
    print("=== Day 1 ===")
    day = 1
    rose.get_info()
    while day < 7:
        rose.grow()
        rose.grow_older()
        day += 1
    print(f"=== Day {day} ===")
    rose.get_info()
    print("Growth this week: +6cm")
