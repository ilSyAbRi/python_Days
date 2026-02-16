class SecurePlant:
    """A plant with secure height and age to prevent invalid updates."""
    def __init__(self, name):
        """Initialize plant with name and default height/age of 0."""
        self.name = name
        self.__height = 0
        self.__age = 0
        print("Plant created:", self.name)

    def set_height(self, height):
        """Set the plant's height if non-negative; reject negative values."""
        if (height < 0):
            print("\nInvalid operation attempted: height " +
                  str(height) + "cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print("Height updated:" + str(self.__height) + "cm [OK]")

    def set_age(self, age):
        """Set the plant's age if non-negative; reject negative values."""
        if (age < 0):
            print("\nInvalid operation attempted: age", age, "[REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print("Age updated:", self.__age, "days [OK]")

    def get_height(self):
        """Return the plant's height."""
        return self.__height

    def get_age(self):
        """Return the plant's age."""
        return self.__age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    print("\nCurrent plant: " + plant.name + " ("
          + str(plant.get_height()) + "cm, "
          + str(plant.get_age()) + " days)")
