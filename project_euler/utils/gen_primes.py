def sieve_eratosthenes(limit, return_primes=True):
    arr = [False, False] + [True] * (limit - 1)
    for n in range(2, int(limit ** 0.5) + 1):
        if arr[n]:
            for k in range(2, limit // n + 1):
                arr[k * n] = False
    if return_primes:
        return [n for n, is_prime in enumerate(arr) if is_prime]
    return arr

primes = sieve_eratosthenes(limit=int(1e8))

with open('primes_below_1e8.txt', 'w+') as fp:
    for p in primes:
        fp.write(str(p) + '\n')