import random


def gen_player_achievements() -> set:
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
    number = random.randint(1, 4)
    return set(random.sample(all_achievements, number))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print("Player Alice: ", gen_player_achievements())
    