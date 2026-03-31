from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===")
    my_deck = Deck()
    game_state = {"mana": 20}

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    bolt = SpellCard("Lightning Bolt", 3, "Common", "Fire")
    Crystal = ArtifactCard("Mana Crystal", 4, "Rare", 5, "+1 Mana per turn")

    my_deck.add_card(dragon)
    my_deck.add_card(bolt)
    my_deck.add_card(Crystal)

    stats = my_deck.get_deck_stats()
    print("\nBuilding deck with different card types...")
    print(f"Deck stats: {stats}")

    print("\nDrawing and playing cards:")

    for _ in range(3):
        my_deck.shuffle()
        drawn_card = my_deck.draw_card()
        if drawn_card:
            type_label = drawn_card.__class__.__name__.replace("Card", "")
            print(f"\nDrew: {drawn_card.name} ({type_label})")
            print(f"Play Result: {drawn_card.play(game_state)}")

    print("\nPolymorphism in action: Same interface,\
different card behaviors!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error :", e)
