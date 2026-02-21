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



class PlantError(GardenError):
    """Raised for plant-specific problems."""
    pass

class WaterError(GardenError):
    """Raised for watering issues."""
    pass
