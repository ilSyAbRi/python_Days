from ex0 import FlameFactory, AquaFactory

def test_factory(factory):
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing factory")

    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack())

def battle(factory1, factory2):

    base_creature1 = factory1.create_base()
    base_creature2 = factory2.create_base()
    
    print(base_creature1.describe())
    print("vs.")
    print(base_creature2.describe())

    print("fight!")
    print(base_creature1.attack())
    print(base_creature2.attack())
