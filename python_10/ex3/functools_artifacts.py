import functools
import operator
from typing import Any
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    tools = {
        'add': operator.add, 'multiply': operator.mul, 'max': max, 'min': min}
    return functools.reduce(tools.get(operation, operator.add), spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'Fire': functools.partial(base_enchantment, 50, 'Fire'),
        'Ice': functools.partial(base_enchantment, 50, 'Ice'),
        'Storm': functools.partial(base_enchantment, 50, 'Storm')
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable:
    @functools.singledispatch
    def run(spell: Any) -> str: return "Unknown spell type"

    @run.register(int)
    def _(val: int): return f"Damage spell: {val} damage"

    @run.register(str)
    def _(val: str): return f"Enchantment: {val}"

    @run.register(list)
    def _(val: list): return f"Multi-cast: {len(val)} spells"

    return run


if __name__ == "__main__":
    print("Testing spell reducer...")
    nums = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(nums, 'add')}")
    print(f"Product: {spell_reducer(nums, 'multiply')}")
    print(f"Max: {spell_reducer(nums, 'max')}")

    print("\nTesting memoized fibonacci...")
    for i in [0, 1, 10, 15]:
        print(f"Fib({i}): {memoized_fibonacci(i)}")

    print("\nTesting spell dispatcher...")
    d = spell_dispatcher()
    print(d(42))
    print(d("fireball"))
    print(d([1, 2, 3]))
    print(d(10.5))
