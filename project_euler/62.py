from collections import defaultdict

def int2idx(n):
    # give an index to each integer, that is unique modulo permutation (eg id of 55416 = id of 51645)
    digits = defaultdict(int)
    for digit in list(str(n)):
        digits[digit] += 1
    idx = ''
    for k in sorted(digits.keys()):
        idx += f'{digits[k]}*{k},'
    return idx

print(int2idx(55416))
print(int2idx(51645))
print(int2idx(511645))

def solve(N):
    count_hits = defaultdict(list)

    # go through all cubes until we hit N permutations
    n = 1
    while True:
        cube = n ** 3
        idx = int2idx(cube)
        count_hits[idx].append(cube)
        if len(count_hits[idx]) == N:
            print(count_hits[idx])
            print('ans:', count_hits[idx][0])
            break
        n += 1

solve(3)
solve(5)