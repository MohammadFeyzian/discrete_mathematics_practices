# Calculate the factorial of n with iterative approach
def factorial(n):
    assert n > 0
    result = 1
    for i in range(1, n + 1):
        result *= i

    print(f"Factorial of {n} is: {result}")


factorial(5)
