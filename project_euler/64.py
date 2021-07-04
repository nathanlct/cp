"""
N = 23
sqrt(23) = 4, remainder = 23 - 16 = 7

sqrt(23) = 4 + (sqrt(23) - 4) / 1
sqrt(23) = 4 + 1 / ((sqrt(23) + 4) / 7)

(sqrt(23) + 4) / 7 = 1 + (-7 + sqrt(23) + 4) / 7
                   = 1 + (sqrt(23) - 3) / 7
                   = 1 + 1 / (7 * (sqrt(23) + 3)) / 14

7 * (sqrt(23) + 3) / 14 = 3 + (-14 * 3 + 7 sqrt(23) + 21) / 14
                        = 3 + (7 sqrt(23) - 21) / 14
                        = 3 + (49 * 23 - 21 * 21) / 14 (7 sqrt(23) + 21)
                        = 3 + 49 / (7 sqrt(23) + 21)
                        = 3 + 1 / (7 sqrt(23) + 21) / 49
faster : 7 * (sqrt(23) + 3) / 14 = (sqrt(23) + 3) / 2

expected = 4 (1 3 1 8)

x = (sqrt(n) + a) / b
m = int(x)
x = m + (sqrt(n) + (a - b * m)) / b
  = m + (n - (a - b * m) ^ 2) / b * (sqrt(n) - (a - b * m))
  = m + 1 / new_x
with new_x = (sqrt(n) - (a - b * m)) / ((n - (a - b * m) ^ 2) / b)
"""

from math import sqrt

def get_coefs(n):
    coefs = []
    a = 0
    b = 1

    while True:
        m = int((sqrt(n) + a) / b)
        a, b = - (a - b * m), (n - (a - b * m) ** 2) // b

        if b == 0:  # n is a perfect square
            return None

        if (m, a, b) in coefs:
            idx_start = coefs.index((m, a, b))
            return (
                [c[0] for c in coefs[:idx_start]],
                [c[0] for c in coefs[idx_start:]]
            )

        coefs.append((m, a, b))

def solve(N):
    ans = 0
    for i in range(2, N + 1):
        coefs = get_coefs(i)
        if coefs is not None and len(coefs[1]) % 2 == 1:
            ans += 1
    return ans

print(solve(13))
print(solve(10000))


# can we calculate square roots now
n = 2
print(f'bonus, compute sqrt({n})')
coefs = get_coefs(n)
for n_approx in range(1, 20):
    # get the right nb of coefs
    approx_coefs = coefs[0]
    while len(approx_coefs) < n_approx:
        approx_coefs += coefs[1]
    approx_coefs = approx_coefs[:n_approx]

    # compute result
    res = approx_coefs[-1]
    for coef in approx_coefs[:-1][::-1]:
        res = coef + 1 / res
    print(res, f'(approx with {n_approx} coefs), precision = ', abs(sqrt(n) - res))
# well thats the next problem actually lol

