class Plant:
    """A plant with name, height, and age."""
    def __init__(self, name, height, age):
        """Initialize plant with name, height (cm), and age (days)."""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        """Return a string summarizing the plant."""
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


plants_data = [
    Plant("Rose", 25, 30),
    Plant("Oak", 200, 365),
    Plant("Cactus", 5, 90),
    Plant("Sunflower", 80, 45),
    Plant("Fern", 15, 120)
]

print("=== Plant Factory Output ===")
for p in plants_data:
    print(p.get_info())
print("\nTotal plants created: 5")
