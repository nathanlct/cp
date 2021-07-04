from math import sqrt

def solve(N):
    # compute coefs
    coefs = [2]
    while len(coefs) < N:
        coefs += [1, 2 * (1 + (len(coefs) - 1) // 3), 1]
    coefs = coefs[:N]

    # compute result
    top, bot = coefs[-1], 1
    for coef in coefs[:-1][::-1]:
        top, bot = coef * top + bot, top

    return sum(map(int, list(str(top))))

print(solve(10))
print(solve(100))