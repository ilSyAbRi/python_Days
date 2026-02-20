class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised for problems related to plants."""
    pass


class WaterError(GardenError):
    """Raised for problems related to watering."""
    pass


def check_plant():
    """Simulate a plant check and raise PlantError if the plant is wilting."""
    raise PlantError("The tomato plant is wilting!")


def check_water():
    """Simulate a water check and raise WaterError if water is insufficient."""
    raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_plant()
    except PlantError as e:
        print("Caught PlantError:", e)

    print("\nTesting WaterError...")
    try:
        check_water()
    except WaterError as e:
        print("Caught WaterError:", e)

    print("\nTesting catching all garden errors...")

    try:
        check_plant()
    except GardenError as e:
        print("Caught a garden error:", e)

    try:
        check_water()
    except GardenError as e:
        print("Caught a garden error:", e)

    print("\nAll custom error types work correctly!")
