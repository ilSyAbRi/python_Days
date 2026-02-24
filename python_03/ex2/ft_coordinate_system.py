import math

def coordinate_system():
    print("=== Game Coordinate System ===")

    position = (10, 20, 5)
    print("Position created:" position)

    origin = (0, 0, 0)

    x1, y1, z1 = origin
    x2, y2, z2 = position
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between {origin} and {position}: {round(distance, 2)}")
