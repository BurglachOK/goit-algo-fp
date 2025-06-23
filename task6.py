
def greedy_algorithm(items, budget):
    quantity = 0
    result = {}
    for i in [x[0] for x in sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)]:
        while items[i]['cost'] <= budget:
            budget -= items[i]['cost']
            quantity += 1
            result[i] = result.get(i, 0) + 1
        quantity = 0
    return result


def dynamic_programming(items, budget):
    res = [0]
    for i in range(1, budget + 1):
        res.append(float('-inf'))
        for j in items.keys():
            if items[j]['cost'] <= i:
                if res[i - items[j]['cost']] + items[j]['calories'] > res[i]:
                    res[i] = res[i - items[j]['cost']] + items[j]['calories']
        if res[-1] == float('-inf'):
            res[-1] = 0
            
    print(res)
    return backtrack(res, budget)


def backtrack(res, t):
    items_result = {item[0]: 0 for item in sorted(items.items())}
    while t > 0:
        items_left = res[t]
        temp = {}
        for item in items:
            temp[item] = res[t - items[item]['cost']]
            if res > items[item]['calories']:
                'do'
            # if res[t - items[item]['cost']] == items_left - 1:
                items_result[item] += 1
                t -= items[item]['cost']
                break
    return {item: items_result[item] for item in items if items_result[item] != 0}




items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}}
budget = 100
print(greedy_algorithm(items, budget))
print(dynamic_programming(items, budget))
