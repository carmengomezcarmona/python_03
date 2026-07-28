import math


def get_player_pos() -> tuple[float, float, float]:
    valid = False
    while not valid:
        coordinates = input("Enter new coordinates as floats in format"
                            "'x,y,z': ")
        parts = coordinates.split(",")
        if len(parts) == 3:
            try:
                x = float(parts[0])
                y = float(parts[1])
                z = float(parts[2])
                coordinates_tuple = (x, y, z)
                valid = True
            except ValueError as e:
                print(f"Error on parameter: {e}")
        else:
            print("Invalid syntax")
    return coordinates_tuple


def calculate_distance(position: tuple[float, float, float]) -> float:
    distance = math.sqrt(
        position[0] ** 2 +
        position[1] ** 2 +
        position[2] ** 2
    )
    return distance


def calculate_distance_between(first: tuple[float, float, float], second:
                               tuple[float, float, float]) -> float:
    dx = second[0] - first[0]
    dy = second[1] - first[1]
    dz = second[2] - first[2]
    distance_between = math.sqrt(dx**2 + dy**2 + dz**2)
    return distance_between


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    first_position = get_player_pos()
    distance = calculate_distance(first_position)
    print("Got a first tuple:", first_position)
    print(f"It includes: X={first_position[0]}, Y={first_position[1]}, "
          f"Z={first_position[2]}")
    print("Distance from origin:", round(distance, 4))
    print()
    print("Get a second set of coordinates")
    second_position = get_player_pos()
    distance_between = calculate_distance_between(first_position,
                                                  second_position)
    print("Distance between the 2 sets of coordinates:",
          round(distance_between, 4))
