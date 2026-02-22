def check_temperature(temp_str):
    """
    Converts a string to a number
    and checks if it is a valid plant temperature (0–40°C).
    """
    try:
        temp = int(temp_str)
        print(f"\nTesting temperature: {temp}")
        if temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
            return None
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
            return None
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp
    except ValueError:
        print(f"\nTesting temperature: {temp_str}")
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input():
    """Tests check_temperature with different inputs."""

    print("=== Garden Temperature Checker ===")
    check_temperature("25")

    check_temperature("abc")

    check_temperature("100")

    check_temperature("-50")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
