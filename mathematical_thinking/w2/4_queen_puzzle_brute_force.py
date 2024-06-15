import itertools

# Find the positions of n queen in an n * n chess board without attacking each other
# Brute Force solution:
#   create all the possible permutations
#   iterate over them one by one, and check if they are valid or not
#   The formula for validation is:


def is_solution(perm):
    for (i1, i2) in itertools.combinations(range(len(perm)), 2):
        # print(f"i1 = {i1}, i2 = {i2} -> j1 = {perm[i1]}, j2 = {perm[i2]}")
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False
    return True


def check_all_cases(size):
    perms = itertools.permutations(range(size))
    for perm in perms:
        if is_solution(perm):
            print(perm)


check_all_cases(4)