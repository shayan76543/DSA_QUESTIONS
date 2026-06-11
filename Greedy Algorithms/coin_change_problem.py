def coin_change_problem(coins, amount):
    count = 0
    coins.sort(reverse=True)
    for coin in coins:
        while coin <= amount:
            amount -= coin
            count += 1
    return count
print(coin_change_problem([1, 2, 5, 10, 20, 50, 100, 500, 1000], 1343))
