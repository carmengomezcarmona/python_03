import sys


def check_arguments(argv: list[str]) -> list[int]:
    print("=== Player Score Analytics ===")
    valid_scores = []
    for i in range(1, len(argv)):
        try:
            valid_scores.append(int(argv[i]))
        except ValueError:
            print(f"Invalid parameter: '{argv[i]}'")
    if len(valid_scores) < 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ... ")
    else:
        total_players = len(valid_scores)
        total_score = sum(valid_scores)
        average_score = total_score / total_players
        high_score = max(valid_scores)
        low_score = min(valid_scores)
        score_range = high_score - low_score
        print("Scores processed:", valid_scores)
        print("Total players:", total_players)
        print("Total score:", total_score)
        print("Average score:", average_score)
        print("High score:", high_score)
        print("Low score:", low_score)
        print("Score range:", score_range)
    return valid_scores


check_arguments(sys.argv)
