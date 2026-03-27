from abc import ABC, abstractmethod


class Card (ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> None:
        pass

    def get_card_info(self) -> str:
        return f"{self.name} (Cost: {self.cost}, Rarity: {self.rarity})"
    
    def is_playable(self, available_mana: int) -> bool:
        return self.cost <= available_mana