my_dict = {
    "alice": [
        "first_blood",
        "pixel_perfect",
        "speed_runner",
        "first_blood",
        "first_blood",
    ],
    "bob": [
        "level_master",
        "boss_hunter",
        "treasure_seeker",
        "level_master",
        "level_master",
    ],
    "charlie": [
        "treasure_seeker",
        "boss_hunter",
        "combo_king",
        "first_blood",
        "boss_hunter",
        "first_blood",
        "boss_hunter",
        "first_blood",
    ],
}

if __name__ == "__main__":
    print("=== Achievement Tracker System ===")

    alice = set(my_dict["alice"])
    bob = set(my_dict["bob"])
    charlie = set(my_dict["charlie"])

    print("\nPlayer alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)

    print("\n=== Achievement Analytics ===")

    all_achievements = alice.union(bob).union(charlie)
    print("All unique achievements:", all_achievements)

    print("Total unique achievements:", len(all_achievements))

    common_all = alice.intersection(bob).intersection(charlie)
    print("\nCommon to all players:", common_all)

    alice_bob_shared = alice.intersection(bob)
    alice_charlie_shared = alice.intersection(charlie)
    bob_charlie_shared = bob.intersection(charlie)

    shared = (
            alice_bob_shared
            .union(alice_charlie_shared)
            .union(bob_charlie_shared)
            )
    rare = all_achievements.difference(shared)

    print("Rare achievements (1 player):", rare)

    print("\nAlice vs Bob common:", alice.intersection(bob))

    print("Alice unique:", alice.difference(bob))

    print("Bob unique:", bob.difference(alice))
