from abc import ABC, abstractmethod
from ex1.capabilities import HealCapability

class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature):
        pass

    @abstractmethod
    def is_valid(self, creature):
        pass

class NormalStrategy(BattleStrategy):
    def is_valid(self, creature):
        return True

    def act(self, creature):
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )

        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature):
        return hasattr(creature, "transform") and callable(creature.transform)

    def act(self, creature):
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{creature.name}' for this aggressive strategy")
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature):
        return isinstance(creature, HealCapability)

    def act(self, creature):
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature.name}' for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())
