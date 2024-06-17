def factorial(n):
    assert n > 0
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = 5
print(f"Factorial of {n} is {factorial(n)}")
