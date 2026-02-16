class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    def __init__(self, name, height, flower_color):
        super().__init__(name, height)
        self.flower_color = flower_color
        self.is_blooming = True


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, flower_color, prize_points):
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points

class GardenManager:
    all_gardens = []

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        GardenManager.all_gardens.append(self)

    def add_plant(self,plant):
        self.plants.append(plant)

    def grow_all_plants(self):
        for plant in self.plants:
            plant.height += 1


    class GardenStats:
        def __init__(self, garden):
            self.garden = garden
        
        def plant_count(self):
            return len(self.garden.plants)

        def total_growth(self):
            total = 0
            for plant in self.garden.plants:
                total += plant.height
            return total

        def plant_types(self):
            plants = 0
            flowering = 0
            prize = 0

            for plant in self.garden.plants:
                if type(plant) == PrizeFlower:
                    prize += 1
                elif type(plant) == FloweringPlant:
                    flowering += 1
                else:
                    plant += 1
            return plants, flowering, prize

alice = GardenManager("Alice")
rose = FloweringPlant("Rose", 25, "Red")
sunflower = PrizeFlower("Sunflower", 50, "Yellow", 10)

alice.add_plant(rose)
alice.add_plant(sunflower)

alice_stats = GardenManager.GardenStats(alice)

print("Total growth:", alice_stats.total_growth())
print("Number of plants:", alice_stats.plant_count())
plants, flowering, prize = alice_stats.plant_types()
print("Plants:", plants)
print("Flowering Plants:", flowering)
print("Prize Flowers:", prize)
