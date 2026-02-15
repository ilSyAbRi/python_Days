class Plant:
    """A plant with name, height, and age."""
    def __init__(box, name, height, age):
        """Initialize plant with name, height (cm), and age (days)."""
        box.name = name
        box.height = height
        box.age = age

    def get_info(box):
        """Return plant info as a string."""
        return f"{box.name}: {box.height}cm, {box.age} days old"


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)

print("=== Garden Plant Registry ===")
print(rose.get_info())
print(sunflower.get_info())
print(cactus.get_info())
