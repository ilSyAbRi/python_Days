from ex0.creatures import Flameling
from ex1.capabilities import Sproutling, Shiftling
from ex2.strategies import NormalStrategy, DefensiveStrategy, AggressiveStrategy


def main():

    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    aggressive = AggressiveStrategy()

    flameling = Flameling()
    sproutling = Sproutling()
    shiftling = Shiftling()

    print("\nTournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")
    print("* Battle *")
    print(flameling.describe())
    print("vs.")
    print(sproutling.describe())
    print("now fight!")
    normal.act(flameling)
    defensive.act(sproutling)

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    print("2 opponents involved")
    print("* Battle *")
    print(flameling.describe())
    print("vs.")
    print(sproutling.describe())
    print("now fight!")
    try:
        aggressive.act(flameling)
    except ValueError as e:
        print("Battle error, aborting tournament:", e)
    defensive.act(sproutling)

    print("\nTournament 2 (multiple)")
    print("[ (Flameling+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    print("3 opponents involved")
    
    print("\n* Battle *")
    print(flameling.describe())
    print("vs.")
    print(sproutling.describe())
    print("now fight!")
    normal.act(flameling)
    defensive.act(sproutling)

    print("\n* Battle *")
    print(flameling.describe())
    print("vs.")
    print(shiftling.describe())
    print("now fight!")
    normal.act(flameling)
    aggressive.act(shiftling)

    print("\n* Battle *")
    print(sproutling.describe())
    print("vs.")
    print(shiftling.describe())
    print("now fight!")
    defensive.act(sproutling)
    aggressive.act(shiftling)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error :", e)
