# Generate all the permutations of range (0, n) with back tracking

def generate_all_permutations(perm, n, counter):

    if len(perm) == n:
        counter[0] += 1
        print(f"Solution {counter[0]}")
        print(perm)

    for k in range(n):
        if k not in perm:
            perm.append(k)

            # Check and see if adding the new one is valid or not
            if can_be_extended_to_solution(perm):
                generate_all_permutations(perm, n, counter)

            perm.pop()


def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True


generate_all_permutations([], 8, [0])
