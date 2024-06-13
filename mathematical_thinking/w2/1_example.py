# Print the six-digits number that is divisible by 9127 and start with 100
# The number should be between 100,000 and 100,999
# Paper solution:
#   we start from 100,000 and divide it by 9127 to get the remainder
#   100,000 % 9127 The remainder is 10.9565 and the closes number to it is 11
#   So, 11 * 9127 = 100397
# -----------------
# Code solution
def find_number():
    print("Star t")
    num = 0
    for i in range(100000, 100999):
        if i % 9127 == 0:
            num = i
            break

    print_number(num)


def print_number(num):
    if num > 0:
        print("Number is " + str(num))
    else:
        print("There is no such a number")


find_number()
