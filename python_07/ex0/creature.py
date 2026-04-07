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

class CreatureFactory(ABC):
    @abstractmethod
    def create_base():
        pass


    def create_evolved():
        pass

class FlameFactory(CreatureFactory):
    pass

class AquaFactory(CreatureFactory):
    pass
