def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None or plant == "":
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
        print("Watering completed successfully!")
    except ValueError as e:
        print("Error:", e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    good_list = ["tomato", "lettuce", "carrots"]
    water_plants(good_list)

    print("Testing with error...")
    bad_list = ["tomato", None, "carrots"]
    water_plants(bad_list)

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
