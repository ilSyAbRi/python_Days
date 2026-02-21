class GardenError(Exception):
    """Base class for all garden errors."""
    def __init__(self):
        self.plants = []

    def add_plant(self, name):
        """Add a plant with validation."""
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self.plants.append(name)
        print(f"Added {name} successfully")

    def water_plants(self):
        """Water all plants safely."""
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant == "":
                    raise PlantError("Cannot water an empty plant!")
                print(f"Watering {plant} - success")
        except PlantError as e:
            print(f"Error watering plant: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, plant, water, sun):
        """Check plant health and raise errors if levels are wrong."""
        try:
            if water < 1:
                raise WaterError(f"Water level {water} too low (min 1)")
            if water > 10:
                raise WaterError(f"Water level {water} too high (max 10)")
            if sun < 2:
                raise PlantError(f"Sunlight {sun} too low (min 2h)")
            if sun > 12:
                raise PlantError(f"Sunlight {sun} too high (max 12h)")
            print(f"{plant}: healthy (water: {water}, sun: {sun})")
        except GardenError as e:
            print(f"Error checking {plant}: {e}")


class PlantError(GardenError):
    """Raised for plant-specific problems."""
    pass

class WaterError(GardenError):
    """Raised for watering issues."""
    pass

if __name__ == "__main__":
    print("=== Garden Management System ===")
    garden = GardenManager()
    print("Adding plants to garden...")
    for name in ["tomato", "lettuce", ""]:
        try:
            garden.add_plant(name)
        except PlantError as e:
            print(f"Error adding plant: {e}")
    print("Watering plants...")
    garden.water_plants()
    print("Checking plant health...")
    garden.check_health("tomato", 5, 8)
    garden.check_health("lettuce", 15, 6)
    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")
