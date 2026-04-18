from collections.abc import Callable
from typing import Any

def mage_counter() -> Callable[[], int]:
    count = 0
    def add_one() -> int:
        nonlocal count
        count += 1
        return count
    return add_one

def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    current_total = initial_power
    def update(bonus: int) -> int:
        nonlocal current_total
        current_total += bonus
        return current_total
    return update

def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def label(item: str) -> str:
        return f"{enchantment_type} {item}"
    return label

def memory_vault() -> dict[str, Callable]:
    safe_box = {}
    def store(key: str, val: Any): safe_box[key] = val
    def recall(key: str): return safe_box.get(key, "Memory not found")
    return {"store": store, "recall": recall}

if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("\nTesting enchantment factory...")
    print(enchantment_factory("Flaming")("Sword"))
    print(enchantment_factory("Frozen")("Shield"))

    print("\nTesting memory vault...")
    v = memory_vault()
    v['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {v['recall']('secret')}")
    print(f"Recall 'unknown': {v['recall']('unknown')}")
