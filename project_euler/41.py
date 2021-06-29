
def gen_permutations(arr):
    if len(arr) == 1:
        yield arr
    for first_digit in arr: #sorted(arr):
        other_digits = [d for d in arr if d != first_digit]
        sub_permutations = gen_permutations(other_digits)
        for perm in sub_permutations:
            yield [first_digit] + perm

def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return (n == 2)
    for k in range(3, n, 2):
        if n % k == 0: return False
    return True

for N in range(9, 2, -1):
    permutations = gen_permutations(list(range(1, N+1))[::-1])
    for i, perm in enumerate(permutations):
        if is_prime(p := int(''.join(map(str, perm)))):
            print(p)
            import sys; sys.exit(0)