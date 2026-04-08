from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type_: str):
        self.name = name
        self.type = type_

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"

    @abstractmethod
    def attack(self) -> str:
        pass


class Flameling(Creature):
    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"


class CreatureFactory:
    def create_base(self):
        pass

    def create_evolved(self):
        pass


class FlameFactory(CreatureFactory):
    pass


class AquaFactory(CreatureFactory):
    pass
