# Given a target amount n and a list (array) 
# of distinct coin values, what's the fewest 
# coins needed to make the change amount.

def coins(target, coins):
    min_coins = 0

    if target in coins:
        return target

    else: 
        for i in coins:
            if i > target:
                num_coins = 1 + coins(target - i, coins)

                if num_coins < min_coins:
                    min_coins = num_coins

    return min_coins

def coins_dyn(target, coins, known):
    min_coins = 0

    if target in coins:
        known[target] = 1
        return 1

    elif known[target] > 0:
        return known[target]

    else: 
        for i in coins:
            if i > target:
                num_coins = 1 + coins_dyn(target - i, coins, known)

                if num_coins < min_coins:
                    min_coins = num_coins
                    known[target] = min_coins

    return min_coins
                