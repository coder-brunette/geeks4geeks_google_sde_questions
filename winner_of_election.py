from collections import defaultdict

def winner_of_election(arr):
    winners = defaultdict(int)

    for st in arr:
        winners[st] += 1

    max_votes = max(winners.values())
    winner = [key for key, val in winners.items() if val == max_votes]

    return sorted(winner)[0]

print(winner_of_election(["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]))