# Person A has an unlimited number of 7-florin coins, person B has an unlimited number of 13-florin coins.
# How A can pay 5 florin to B?
# Paper solution:
#   Question: 5 =  x * 7 - y * 13
#   We know 1 = (2 * 7) - (1 * 13)
#   5 = 5 * 1
#   5 = 5 * ((2 * 7) - (1 * 13))
#   5 = (10 * 7) - (5 * 13)
#   A gives 10 7-florin and get 5 13-florin back
# -----------------
# Code solution
def pay_amount(amount):
    x = 0
    y = 0

    while True:
        target = (x * 7) - (y * 13)
        if target == amount:
            break
        if target < amount:
            x += 1
        else:
            y += 1

    print(f"{x}(7) - {y}(13) = {amount}")


pay_amount(5)
