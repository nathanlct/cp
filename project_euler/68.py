"""
try a faster approach

we're only interested in 16 digit strings
    => 10 must be on an outter node (otherwise it's counted twice in the string)
then we only have to generate the inner ring, the outter ring will be forced since we will already have 1 total
"""

max_val = 0
for a1 in range(1, 10):
    for a2 in range(1, 10):
        for a3 in range(1, 10):
            for a4 in range(1, 10):
                for a5 in range(1, 10):
                    r1 = 10
                    linesum = r1 + a1 + a2
                    r2 = linesum - a2 - a3
                    r3 = linesum - a3 - a4
                    r4 = linesum - a4 - a5
                    r5 = linesum - a5 - a1

                    if set([a1, a2, a3, a4, a5, r1, r2, r3, r4, r5]) == set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
                        lines = [(r1, a1, a2), (r2, a2, a3), (r3, a3, a4), (r4, a4, a5), (r5, a5, a1)]
                        start_idx = lines.index(min(lines))
                        s = ''
                        for i in range(len(lines)):
                            el = lines[(start_idx + i) % len(lines)]
                            s += ''.join(map(str, el))
                        max_val = max(max_val, int(s))
                        print(s)

print('ans', max_val)


def solve_brute_force(N):
    def gen_permutations(arr):
        if len(arr) == 1:
            yield arr
        for first_digit in sorted(arr):
            other_digits = [d for d in arr if d != first_digit]
            sub_permutations = gen_permutations(other_digits)
            for perm in sub_permutations:
                yield [first_digit] + perm

    max_val = 0

    permutations = gen_permutations(list(range(1, 2 * N + 1)))
    for i, perm in enumerate(permutations):
        if i % 10000 == 0:
            print(i, perm)

        # first N digits are inner ring, last N digits are outter nodes

        # to get unique solutions, force position of lowest outter node
        if min(perm[N:]) != perm[N]:
            continue

        # test if all lines sum to the same number
        lines = [(perm[N+k], perm[k], perm[(k+1)%N]) for k in range(N)]
        lines_sums = [sum(line) for line in lines]
        if len(set(lines_sums)) != 1:
            continue
            
        # compute string
        s = ''.join([''.join(map(str, el)) for el in lines])
        if N != 5 or len(s) == 16:
            max_val = max(max_val, int(s))

    return max_val


# print(solve_brute_force(3))
# print(solve_brute_force(5))