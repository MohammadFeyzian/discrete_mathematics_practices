# There exists a three-digit number N that produces remainder 1 when divided by 2,3,4,5,6,7
# Paper solution:
#   1 divided by any number grater than 1, remainder would be 1
#   but 1 is one-digit
#   What about N - 1?
#   Assume k = 2,3,4,5,6,7
#   N - 1 is divisible by k
#   (N - 1) % k = 0
#   What is divisible by k?
#   Multiply the k numbers -> 4 = 2 * 2 and 6 = 2 * 3
#   So: the minimum multiply k can be 2 * 2 * 3 * 5 * 7 = 420
#   N - 1 = 420 -> N = 421
#   Other number?
#   Go one number more
#   N - 1 = 2 * 3 * 4 * 5 * 7 = 840
#   N = 841
#
# -----------------
# Code solution
def find_number():
    ans = []
    for i in range(100, 999):
        if i % 2 == 1 and i % 3 == 1 and i % 4 == 1 and i % 5 == 1 and i % 6 == 1 and i % 7 == 1:
            ans.append(i)

    print(f"Answers: {ans}")


def print_number(num):
    if num > 0:
        print("Number is " + str(num))
    else:
        print("There is no such a number")


find_number()
