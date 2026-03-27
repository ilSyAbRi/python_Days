from ex0.CreatureCard import CreatureCard


def do_Playable_Test(card_name: str, available_mana: int) -> None:
    if card_name.is_playable(available_mana):
        print("Playable:", True)
    else:
        print("Playable:", False)


def main() -> None:
    dragon = CreatureCard("Fire Dragon", 5, "Rare", 7, 5)
    print(dragon.get_card_info())
    do_Playable_Test(dragon, 6)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
