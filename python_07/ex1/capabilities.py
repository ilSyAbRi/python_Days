from ABC import abc, abstractmethod

class BattleStrategy(abc):
    @abstractmethod
    def act(self):
        pass

    @abstractmethod
    def is_valid(abc):
        pass

class NormalStrategy(BattleStrategy):
    pass


class AggressiveStrategy(BattleStrategy):
    pass

class DefensiveStrategy(BattleStrategy):
    pass
