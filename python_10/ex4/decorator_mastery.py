import functools
import time
from typing import Any
from collections.abc import Callable

def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        t1 = time.perf_counter()
        res = func(*args, **kwargs)
        t2 = time.perf_counter()
        print(f"Spell completed in {t2 - t1:.3f} seconds")
        return res
    return wrapper

def power_validator(min_power: int) -> Callable:
    def deco(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(self, spell_name: str, power: int, *args, **kwargs):
            if power >= min_power:
                return func(self, spell_name, power, *args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return deco

def retry_spell(max_attempts: int) -> Callable:
    def deco(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {i}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return deco

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"

if __name__ == "__main__":
    print("Testing spell timer...")
    @spell_timer
    def fireball():
        time.sleep(0.101)
        return "Fireball cast!"
    print(f"Result: {fireball()}")

    print("\nTesting retrying spell...")
    @retry_spell(3)
    def broken_spell(): raise Exception("Fail")
    print(broken_spell())
    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild...")
    g = MageGuild()
    print(g.validate_mage_name("Alex"))
    print(g.validate_mage_name("Al"))
    print(g.cast_spell("Lightning", 15))
    print(g.cast_spell("Spark", 5))
