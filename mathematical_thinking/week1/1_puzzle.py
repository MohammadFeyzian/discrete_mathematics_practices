# Find a two-digit number that becomes 57 times smaller after the first digit is deleted
#   We can use find it in this way:
#   ab...z = 57 * b...z
#   X = b...z has k digits
#   a * 10^k + X = 57 * X
#   a * 10^k = 56*X
#   a * 10^k = 56 * X = 7 * 8 * X
#   a divisible by 7: only a = 7 works
#   10^k = 8 * X; 10 and 100 not multiples of 8
#   1000 works, X = 125
#   ab...z = 7125

def find_the_number(num):
    curr = 1
    ans = -1

    while True:
        if curr % num == 0:
            num_str = str(curr)[1:]
            if int(num_str) * num == curr:
                ans = curr
                break

        curr += 1
    return ans


target = 57

print(f"For {target} the result is {find_the_number(target)}")
