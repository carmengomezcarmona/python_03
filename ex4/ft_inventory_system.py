import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for argument in sys.argv[1:]:
        parts = argument.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{argument}'")
            continue
        item = parts[0]
        try:
            quantity = int(parts[1])
        except ValueError as e:
            print(f"Quantity error for '{item}':", e)
            continue
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
        else:
            inventory[item] = quantity
    total = 0
    for item in inventory:
        total = total + inventory[item]
    print("Got inventory:", inventory)
    print("Item list: ", list(inventory.keys()))
    print(f"Total quantity of the {len(item)} items:", total)
    for item in inventory:
        porcentaje = inventory[item] / total * 100
        print(f"Item {item} represents {round(porcentaje, 1)}%")
    max_item = ""
    max_quantity = 0
    for item in inventory:
        if inventory[item] > max_quantity:
            max_quantity = inventory[item]
            max_item = item
    print(f"Item most abundant: {max_item} with quantity {max_quantity}")
    min_item = list(inventory.keys())[0]
    min_quantity = inventory[min_item]
    for item in inventory:
        if inventory[item] < min_quantity:
            min_quantity = inventory[item]
            min_item = item
    print(f"Item least abundant: {min_item} with quantity {min_quantity}")
    inventory["magic_item"] = 1
    print("Updated inventory: ", inventory)
