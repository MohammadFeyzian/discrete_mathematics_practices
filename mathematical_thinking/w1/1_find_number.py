# Find a two-digit number that becomes 57 times smaller after
#   the first digit is deleted

number = 1
ans = -1

while True:
    if number % 57 == 0:
        numStr = str(number)[1:]
        if int(numStr) * 57 == number:
            ans = number
            break

    number += 1

print("Answer is", ans)
