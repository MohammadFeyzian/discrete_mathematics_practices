# Imagine we have only 5- and 7-coins. One can prove that any large enough integer amount
# can be paid using only such coins. Yet clearly we cannot pay any of numbers 1,2,3,4,6,,8,9
# with our coins. What is the maximum amount that cannot be paid?
def can_be_payed(amount):
    if amount == 0:
        return True
    if amount < 5:
        return False
    if amount % 7 == 0:
        return can_be_payed(amount - 7)
    else:
        return can_be_payed(amount - 5)


for i in range(100):
    if can_be_payed(i):
        print(i)