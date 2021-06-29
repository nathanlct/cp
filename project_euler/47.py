from collections import defaultdict


memoiz = {1: []}

def _prime_decomp(n, min_p=2):
    p = 2    
    while True:
        if n % p == 0:
            return [p] + prime_decomp(n // p, min_p=p)
        else:
            p += (1 if p == 2 else 2)

def prime_decomp(n, min_p=2):
    if n not in memoiz:
        memoiz[n] = _prime_decomp(n, min_p=min_p)
    return memoiz[n]


# faster: check with a small number of primes
primes = [2]
for i in range(3, 1000, 2):
    candidate = True
    for k in range(3, int(i ** 0.5) + 1, 2):
        if i % k == 0:
            candidate = False
            break
    if candidate:
        primes.append(i)

def count_factors(n):
    count = 0
    for p in primes:
        if p >= n:
            break
        if n % p == 0:
            count += 1
    return count


def solve(N):
    i = 2
    consecutive_counter = 0
    while consecutive_counter < N:
        # primes = prime_decomp(i)
        # if len(set(primes)) >= N:
        if count_factors(i) >= N:
            consecutive_counter += 1
        else:
            consecutive_counter = 0
        i += 1

    print(i - N)

solve(2)
solve(3)
solve(4)