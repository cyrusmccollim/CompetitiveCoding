args = input().split()
num_ing = int(args[0]) # 3
num_recipe = int(args[1]) # 2

stock = [int(i) for i in input().split()] # [5, 10, 10]

max_money = 0
for i in range(num_recipe):
    recipe = [int(i) for i in input().split()]
    most_usages = float('inf') 
    for ingredient in range(len(stock)):
        if recipe[ingredient] == 0: continue
        usage = stock[ingredient] // recipe[ingredient]
        if usage < most_usages:
            most_usages = usage
    money = most_usages * recipe[-1]
    if money > max_money:
            max_money = money

print(max_money)
