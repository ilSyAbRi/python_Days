from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def run_all(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return run_all


if __name__ == "__main__":
    fire: Callable = lambda t, p: f"Fireball hits {t}"
    heal: Callable = lambda t, p: f"Heals {t}"

    print("Testing spell combiner...")
    both = spell_combiner(fire, heal)
    res = both("Dragon", 50)
    print(f"Combined spell result: {res[0]}, {res[1]}")

    print("\nTesting power amplifier...")
    orig: Callable = lambda t, p: f"{p}"
    boosted = power_amplifier(orig, 3)
    print(f"Original: 10, Amplified: {boosted('Target', 10)}")
