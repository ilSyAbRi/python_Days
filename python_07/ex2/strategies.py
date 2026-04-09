from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature):
        pass

    @abstractmethod
    def is_valid(self, creature):
        pass

class NormalStrategy(BattleStrategy)

class AggressiveStrategy(BattleStrategy)

class DefensiveStrategy(BattleStrategy)
