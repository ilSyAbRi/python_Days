class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def grow_older(self):
        self.age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


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
