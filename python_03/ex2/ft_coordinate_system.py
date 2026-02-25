import math
import sys


def step1():
    print("=== Game Coordinate System ===")

    position = (10, 20, 5)
    print("\nPosition created:", position)

    origin = (0, 0, 0)

    x1, y1, z1 = origin
    x2, y2, z2 = position
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between {origin} and {position}: {round(distance, 2)}")

    coord_str = "3,4,0"
    print(f'\nParsing coordinates: "{coord_str}"')

    vparse = coord_str.split(",")
    parsed_position = (int(vparse[0]), int(vparse[1]), int(vparse[2]))
    print("Parsed position:", parsed_position)

    x2, y2, z2 = parsed_position
    distance2 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between {origin} and {parsed_position}: {distance2}")

    invalid_str = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{invalid_str}"')

    try:
        parts = invalid_str.split(",")
        _ = (int(parts[0]), int(parts[1]), int(parts[2]))
    except Exception as e:
        print("Error parsing coordinates:", e)
        print("Error details - Type:", type(e).__name__, ", Args:", e.args)

    print("\nUnpacking demonstration:")
    x, y, z = parsed_position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def step2():

    if len(sys.argv) != 3:
        print("\nUsage: python3 ft_coordinate_system.py\
start_x,start_y,start_z target_x,target_y,target_z")
        return

    start_str = sys.argv[1]
    target_str = sys.argv[2]

    try:
        s_parts = start_str.split(",")
        t_parts = target_str.split(",")

        start_position = (int(s_parts[0]), int(s_parts[1]), int(s_parts[2]))
        print("\nPosition created:", start_position)

        print(f'Parsing coordinates: "{target_str}"')
        parsed_position = (int(t_parts[0]), int(t_parts[1]), int(t_parts[2]))
        print("Parsed position:", parsed_position)

        x1, y1, z1 = start_position
        x2, y2, z2 = parsed_position
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        print(f"\nDistance between {start_position}\
and {parsed_position}: {round(distance, 2)}")

    except Exception as e:
        print("\nError parsing coordinates:", e)
        print("Error details - Type:", type(e).__name__, ", Args:", e.args)
        return

    print("\nUnpacking demonstration:")
    x, y, z = parsed_position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    step1()
    step2()
