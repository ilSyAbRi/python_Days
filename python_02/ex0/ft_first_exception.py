def check_temperature(temp_str):
    """
    Converts a string to a number
    and checks if it is a valid plant temperature (0–40°C).
    """
    print(f"Testing temperature: {temp}")
    try:
        temp = int(temp_str)
        if (temp > 40)
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        elif (temp < 0)
            print(f"Error: {temp}°C is too cold for plants (min 0°C)"
        else
            print(f"Temperature {temp}°C is perfect for plants!")

        print("All tests completed - program didn't crash!")
    except ValueError:
        print(f"Error: '{temp}' is not a valid number")
