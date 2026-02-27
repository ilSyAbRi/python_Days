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
        "pixel_sword": {"type": "weapon", "value": 150, "rarity": "common"},
        "quantum_ring": {"type": "accessory", "value": 500, "rarity": "rare"},
        "health_byte": {"type": "consumable", "value": 25, "rarity": "common"},
        "data_crystal": {"type": "material", "value": 1000, "rarity": "legendary"},
        "code_bow": {"type": "weapon", "value": 200, "rarity": "uncommon"},
    },
}


def print_player_inventory(player_name):

    player_name = "alice"

    inventory_value = 0
    inventory_item_count = 0

    for item_name in my_dic["players"][player_name]["items"]:

        item_quantity = my_dic["players"][player_name]["items"][item_name]

        item_unit_price = my_dic["catalog"][item_name]["value"]
        item_type = my_dic["catalog"][item_name]["type"]
        item_rarity = my_dic["catalog"][item_name]["rarity"]

        item_total_price = item_quantity * item_unit_price

        inventory_value = inventory_value + item_total_price
        inventory_item_count = inventory_item_count + item_quantity

        print(item_name, "(", item_type, ",", item_rarity, "):",
            item_quantity, "x @", item_unit_price, "=", item_total_price, "gold")

    print("\nInventory value:", inventory_value)
    print("Item count:", inventory_item_count)


def transfer_item(giver_name, receiver_name, item_name, quantity_to_give):
      
    my_dic["players"][giver_name]["items"][item_name] = (
        my_dic["players"][giver_name]["items"][item_name] - quantity_to_give
    )

    if item_name in my_dic["players"][receiver_name]["items"]:
        my_dic["players"][receiver_name]["items"][item_name] = (
            my_dic["players"][receiver_name]["items"]
            [item_name] + quantity_to_give
        )
    else :
        my_dic["players"][receiver_name]["items"][item_name] = quantity_to_give
    print(f"\n=== Transaction: {giver_name.capitalize()} gives "
    f"{receiver_name.capitalize()} {quantity_to_give} {item_name} ===")
    print("Transaction successful!")

print("=== Player Inventory System ===")

player_name = "alice"
print(f"\n=== {player_name.capitalize}'s Inventory ===")
print_player_inventory(player_name)

transfer_item("alice", "bob", "health_byte", 2)
