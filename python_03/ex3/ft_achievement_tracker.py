print("=== Achievement Tracker System ===")

alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
bob = {"first_kill", "level_10", "boss_slayer", "collector"}
charlie = {"level_10", "treasure_hunter", "boss_slayer",
           "speed_demon", "perfectionist"}

print("\nPlayer alice achievements:", alice)
print("Player bob achievements:", bob)
print("Player charlie achievements:", charlie)

print("\n=== Achievement Analytics ===")

all_achievements = alice.union(bob).union(charlie)
print("All unique achievements:", all_achievements)

print("Total unique achievements:", len(all_achievements))

common_all = alice.intersection(bob).intersection(charlie)
print("\nCommon to all players:", common_all)

alice_bob_shared = alice.intersection(bob)
alice_charlie_shared = alice.intersection(charlie)
bob_charlie_shared = bob.intersection(charlie)

shared = alice_bob_shared.union(alice_charlie_shared).union(bob_charlie_shared)
rare = all_achievements.difference(shared)

print("Rare achievements (1 player):", rare)

print("\nAlice vs Bob common:", alice.intersection(bob))

print("Alice unique:", alice.difference(bob))

print("Bob unique:", bob.difference(alice))
