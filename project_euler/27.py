"""
P(n) = n^2 + an + b
|a|, |b| < 1000

Find a, b st N is maximal: for n < N, P(n) is prime
Return ab
"""

"""
P(0) = b has to be prime
P(1) = a+b+1 has to be prime
"""

def _is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return (n == 2)
    for k in range(3, n, 2):
        if n % k == 0: return False
    return True

memoiz = {}
def is_prime(n):
    if n not in memoiz:
        ans = _is_prime(n)
        memoiz[n] = ans
    return memoiz[n]

max_n = 0
argmax_n = (0, 0)
for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while True:
            p = n*n + a*n + b
            if not is_prime(p):
                if n > max_n:
                    max_n = n
                    argmax_n = a, b
                break
            n += 1

print(max_n, argmax_n, argmax_n[0] * argmax_n[1])