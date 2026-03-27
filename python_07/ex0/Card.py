def Card (Abstract):
    def __init__(self,name, cost, rarity):
        self.name = name
        self.cost = cost
        self.rarity = rarity
    @abstractmethod
    def play(game_state):
        pass
    def 