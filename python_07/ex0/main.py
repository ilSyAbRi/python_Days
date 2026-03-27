from ex0.CreatureCard import CreatureCard


def do_Playable_Test(card: CreatureCard, available_mana: int) -> None:
    if card.is_playable(available_mana):
        print("Playable:", True)
    else:
        print("Playable:", False)


def main() -> None:
    print("\n=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("\nCreatureCard Info:")
    print(dragon.get_card_info())
    print("\nPlaying Fire Dragon with 6 mana available:")
    do_Playable_Test(dragon, 6)
    game_state = {"mana": 6}
    result = dragon.play(game_state)
    print(result)

    Goblin = CreatureCard("Goblin Warrior", 2, "Common", 3, 2)
    print("\nFire Dragon attacks Goblin Warrior:")
    attack = dragon.attack_target(Goblin)
    print(attack)
    print("\nTesting insufficient mana (3 available):")
    do_Playable_Test(dragon, 3)
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
