import random


def monte_carlo_simulation(num_experiments):
    """Виконує серію експериментів методом Монте-Карло."""
    results = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    for _ in range(num_experiments):
        results[(random.randint(1, 6) + random.randint(1, 6))] += 1
    for i in results:
        results[i] = str(round(results[i] / num_experiments * 100, 2)) + '%'
    return results


num_experiments = 1000000
print(monte_carlo_simulation(num_experiments))