from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda item: item['power'], reverse=True)


def power_filter(mages: list[dict[str, Any]], min_power: int) -> list[dict[str, Any]]:
    return list(filter(lambda hero: hero['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda name: f"* {name} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    power_list = [m['power'] for m in mages]
    if not power_list:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    return {
        "max_power": max(power_list),
        "min_power": min(power_list),
        "avg_power": round(sum(power_list) / len(power_list), 2)
    }


if __name__ == "__main__":
    print("Testing artifact sorter...")
    stuff = [
        {'name': 'Fire Staff', 'power': 92},
        {'name': 'Crystal Orb', 'power': 85}
    ]
    result = artifact_sorter(stuff)
    print(f"{result[0]['name']} ({result[0]['power']} power) \
comes before {result[1]['name']} ({result[1]['power']} power)")

    print("\nTesting spell transformer...")
    magic_words = ["fireball", "heal", "shield"]
    res = " ".join(spell_transformer(magic_words))
    print(res)