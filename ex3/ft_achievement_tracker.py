import random

all_achievements = [
        "Crafting Genius",
        "World Savior",
        "Untouchable",
        "Strategist",
        "Survivor",
        "Treasure Hunter",
        "Boss Slayer",
        "Unstoppable",
        "Master Explorer",
        "Speed Runner",
        "First Steps",
        "Collector Supreme",
        "Sharp Mind"
    ]


def gen_player_achievements() -> set[str]:
    number = random.randint(3, 8)
    return set(random.sample(all_achievements, number))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print("Player Alice: ", alice)
    print("Player Bob: ", bob)
    print("Player Charlie: ", charlie)
    print("Player Dylan: ", dylan)
    print()
    print("All distinct achievements: ", alice.union(bob, charlie, dylan))
    print()
    print("Common achievements: ", alice.intersection(bob, charlie, dylan))
    print()
    print("Only Alice has: ", alice.difference(bob, charlie, dylan))
    print("Only Bob has: ", bob.difference(alice, charlie, dylan))
    print("Only Charlie has: ", charlie.difference(alice, bob, dylan))
    print("Only Dylan has: ", dylan.difference(alice, bob, charlie))
    print()
    missing = set(all_achievements)
    print("Alice is missing: ", missing.difference(alice))
    print("Bob is missing: ", missing.difference(bob))
    print("Charlie is missing: ", missing.difference(charlie))
    print("Dylan is missing: ", missing.difference(dylan))
