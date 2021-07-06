def prime_factors(n):
    factors = []
    p = 2
    while n > 1:
        if n % p == 0:
            factors.append(p)
            n //= p
        else:
            if p == 2: p += 1
            else: p += 2
    return factors

N = 20

from collections import defaultdict
primes = defaultdict(int)
for i in range(1, N + 1):
    for p in set(factors := prime_factors(i)):
        primes[p] = max(primes[p], factors.count(p))

ans = 1
for k, v in primes.items():
    ans *= k ** v
print(ans)