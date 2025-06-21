
def calory_budget(items, budget):
    for i in items:
        cost = items[i]['cost']
        calories = items[i]['calories']
        efficiency = calories / cost
        items[i]['efficiency'] = round(efficiency, 2)
        cost, calories, efficiency = 0, 0, 0
    return items

    





items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}}
budget = 100
print(calory_budget(items, budget))
