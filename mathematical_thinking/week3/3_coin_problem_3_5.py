# Can we pay any amount greater than 8 with coins of 3 and 5?
def change(amount):
    assert amount >= 8
    if amount == 8:
        return [5, 3]
    if amount == 9:
        return [3, 3, 3]
    if amount == 10:
        return [5, 5]

    coins = change(amount - 3)
    coins.append(3)
    return coins


amount = 29
print(f"Result for {amount} is {change(amount)}")
