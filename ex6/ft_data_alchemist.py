import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    print()
    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam"
    ]
    print("Initial list of players:", players)
    new_list_players = [name.capitalize() for name in players]
    print("New list with all names capitalized:", new_list_players)
    capitalized_names = [name for name in players if name[0].isupper()]
    print("New list of capitalized names only:", capitalized_names)
    scores = {name: random.randint(0, 1000) for name in new_list_players}
    print("Score dict:", scores)
    average = sum(scores.values()) / len(scores)
    print("Score average is:", round(average, 2))
    high_scores = {name: score for name, score in scores.items()
                   if score > average}
    print("High scores:", high_scores)
