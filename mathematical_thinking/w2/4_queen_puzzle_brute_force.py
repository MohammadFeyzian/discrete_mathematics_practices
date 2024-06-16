import itertools

# Find the positions of n queen in an n * n chess board without attacking each other
# Brute Force solution:
#   create all the possible permutations
#   iterate over them one by one, and check if they are valid or not


def is_solution(perm):
    for (i1, i2) in itertools.combinations(range(len(perm)), 2):
        # Check for these columns: i1, i2
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            # difference of col and row is the same, so the 2 are in one diagonal
            return False
    return True


def check_all_cases(size):
    perms = itertools.permutations(range(size))
    for perm in perms:
        # try this perm - e.g: [0,1,2,3]
        if is_solution(perm):
            print(f"This is one solution: {perm}")


check_all_cases(4)