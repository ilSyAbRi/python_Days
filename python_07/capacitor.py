from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main():
    print("\nTesting Creature with healing capability")

    healing_factory = HealingCreatureFactory()

    base = healing_factory.create_base()
    evolved = healing_factory.create_evolved()

    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())

    print("\nTesting Creature with transform capability")

    transform_factory = TransformCreatureFactory()

    base = transform_factory.create_base()
    evolved = transform_factory.create_evolved()

    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error", e)
