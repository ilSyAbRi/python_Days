my_dic = {
    "players": {
        "alice": {
            "items": {
                "pixel_sword": 1,
                "code_bow": 1,
                "health_byte": 1,
                "quantum_ring": 3,
            },
            "total_value": 1875,
            "item_count": 6,
        },
        "bob": {
            "items": {"code_bow": 3, "pixel_sword": 2},
            "total_value": 900,
            "item_count": 5,
        },
        "charlie": {
            "items": {"pixel_sword": 1, "code_bow": 1},
            "total_value": 350,
            "item_count": 2,
        },
        "diana": {
            "items": {
                "code_bow": 3,
                "pixel_sword": 3,
                "health_byte": 3,
                "data_crystal": 3,
            },
            "total_value": 4125,
            "item_count": 12,
        },
    },
    "catalog": {
        "pixel_sword":
        {"type": "weapon", "value": 150, "rarity": "common"},
        "quantum_ring":
        {"type": "accessory", "value": 500, "rarity": "rare"},
        "health_byte":
        {"type": "consumable", "value": 25, "rarity": "common"},
        "data_crystal":
        {"type": "material", "value": 1000, "rarity": "legendary"},
        "code_bow":
        {"type": "weapon", "value": 200, "rarity": "uncommon"},
    },
}


def print_player_inventory(player_name):

    player_data = my_dic["players"].get(player_name)
    if not player_data:
        print("Player not found!")
        return

    items = player_data.get("items")
    if not items:
        print("Inventory is empty.")
        return

    for item_name in my_dic["players"][player_name]["items"]:

        item_quantity = my_dic["players"][player_name]["items"][item_name]

        item_unit_price = my_dic["catalog"][item_name]["value"]
        item_type = my_dic["catalog"][item_name]["type"]
        item_rarity = my_dic["catalog"][item_name]["rarity"]

        item_total_price = item_quantity * item_unit_price

        print(
            item_name,
            "(",
            item_type,
            ",",
            item_rarity,
            "):",
            item_quantity,
            "x @",
            item_unit_price,
            "=",
            item_total_price,
            "gold",
        )

    print("\nInventory value:", player_data.get("total_value", 0))
    print("Item count:", player_data.get("item_count", 0))


def transfer_item(giver_name, receiver_name, item_name, quantity_to_give):

    print(
        f"\n=== Transaction: {giver_name.capitalize()} gives "
        f"{receiver_name.capitalize()} {quantity_to_give} {item_name} ==="
    )

    giver_name_data = my_dic["players"].get(giver_name)
    if not giver_name_data:
        print("Transaction failed! Giver not found.")
        return False

    receiver_name_data = my_dic["players"].get(receiver_name)
    if not receiver_name_data:
        print("Transaction failed! Receiver not found.")
        return False

    if quantity_to_give <= 0:
        print("Transaction failed! Quantity must be positive.")
        return False

    item_quantity = giver_name_data["items"].get(item_name, 0)
    if item_quantity == 0:
        print("Transaction failed! Item not found.")
        return False

    if item_quantity < quantity_to_give:
        print("Transaction failed! Not enough items.")
        return False

    my_dic["players"][giver_name]["items"][item_name] = (
        my_dic["players"][giver_name]["items"][item_name] - quantity_to_give
    )

    my_dic["players"][receiver_name]["items"].update(
        {item_name: my_dic["players"][receiver_name]["items"].get(item_name, 0)
         + quantity_to_give}
    )

    total = 0
    count = 0
    for name in my_dic["players"][giver_name]["items"]:
        if name in my_dic["catalog"]:
            qty = my_dic["players"][giver_name]["items"][name]
            val = my_dic["catalog"][name]["value"]
            total += qty * val
            count += qty

    my_dic["players"][giver_name].update({
        "total_value": total,
        "item_count": count
    })

    total = 0
    count = 0
    for name in my_dic["players"][receiver_name]["items"]:
        if name in my_dic["catalog"]:
            qty = my_dic["players"][receiver_name]["items"][name]
            val = my_dic["catalog"][name]["value"]
            total += qty * val
            count += qty

    my_dic["players"][receiver_name].update({
        "total_value": total,
        "item_count": count
    })

    print("Transaction successful!")
    return True


def inventory_analytics():
    most_valuable_player = None
    max_value = 0
    most_items_player = None
    max_items = 0
    rarest_items = set()

    for player_name in my_dic["players"]:
        player_data = my_dic["players"][player_name]

        total_value = player_data.get("total_value", 0)
        if total_value > max_value:
            max_value = total_value
            most_valuable_player = player_name

        item_count = player_data.get("item_count", 0)
        if item_count > max_items:
            max_items = item_count
            most_items_player = player_name

        for item_name in player_data.get("items", {}):
            if item_name in my_dic["catalog"]:
                rarity = my_dic["catalog"][item_name]["rarity"]
                if rarity == "rare" or rarity == "legendary":
                    rarest_items.add(item_name)

    print("\n=== Inventory Analytics ===")
    print("Most valuable player:", most_valuable_player, f"({max_value} gold)")
    print("Most items:", most_items_player, f"({max_items} items)")
    print("Rarest items:", ", ".join(rarest_items))


print("=== Player Inventory System ===")

player_name = "alice"
print(f"\n=== {player_name.capitalize()}'s Inventory ===")
print_player_inventory(player_name)

result = transfer_item("alice", "bob", "health_byte", 1)

if result:
    print("\n=== Updated Inventories ===")
    print(
        "Alice",
        "health_byte:",
        my_dic["players"]["alice"]["items"]["health_byte"],
    )
    print(
        "Bob",
        "health_byte:",
        my_dic["players"]["bob"]["items"]["health_byte"],
    )
else:
    print("\n=== Inventories not updated ===")
inventory_analytics()
