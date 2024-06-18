# Imagine we have only 5- and 7-coins. return the list of coins for the 24 <= amount <= 100
def change(amount):
    if amount == 24:
        return [5, 5, 7, 7]
    if amount == 25:
        return [5, 5, 5, 5, 5]
    if amount == 26:
        return [5, 7, 7, 7]
    if amount == 28:
        return [7, 7, 7, 7]

    if amount % 7 == 0:
        factor = 7
    else:
        factor = 5

    coins = change(amount - factor)
    coins.append(factor)
    return coins


amount = 60
print(f"Changes for the {amount} are {change(amount)}")