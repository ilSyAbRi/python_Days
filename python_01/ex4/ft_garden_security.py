class SecurePlant:
    def __init__(self, name):
        self.name = name
        self.__height = 0
        self.__age = 0
        print("Plant created:", self.name)

    def set_height(self, height):
        if (height < 0):
            print("\nInvalid operation attempted: height " +
                  str(height) + "cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print("Height updated:" + str(self.__height) + "cm [OK]")

    def set_age(self, age):
        if (age < 0):
            print("\nInvalid operation attempted: age", age, "[REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print("Age updated:", self.__age, "days [OK]")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age


print("=== Garden Security System ===")
plant = SecurePlant("Rose")
plant.set_height(25)
plant.set_age(30)
plant.set_height(-5)

print("\nCurrent plant: " + plant.name + " ("
      + str(plant.get_height()) + "cm, "
      + str(plant.get_age()) + " days)")
