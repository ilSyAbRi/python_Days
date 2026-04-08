from ex0 import FlameFactory, AquaFactory

def test_factory(factory):
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing factory")

    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack())
