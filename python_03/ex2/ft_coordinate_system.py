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

    coord_str = "3,4,0"
    print(f"Parsing coordinates: "{coord_str}"")

    vparse = coord_str.split(",")
    parsed_position = (int(vparse[0]), int(vparse[1]), int(vparse[2]))
    print("Parsed position:", parsed_position)
    
    x2, y2, z2 = parsed_position
    distance2 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between {origin} and {parsed_position}: {distance2}")
