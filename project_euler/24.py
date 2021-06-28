
def gen_permutations(arr):
    if len(arr) == 1:
        yield arr
    for first_digit in sorted(arr):
        other_digits = [d for d in arr if d != first_digit]
        sub_permutations = gen_permutations(other_digits)
        for perm in sub_permutations:
            yield [first_digit] + perm

N = 9
permutations = gen_permutations(list(range(N+1)))
for i, perm in enumerate(permutations):
    if i == int(1e6) - 1:
        perm = ''.join(map(str, perm))
        print(perm)
        break
