N = int(10000)
sieve = [True] * N
sieve[0] = False
sieve[1] = False
for i in range(2, N):
    if sieve[i]:
        k = 2
        while (prod := i * k) < N:
            sieve[prod] = False
            k += 1

primes = set([i for i, v in enumerate(sieve) if i >= 1000 and v])

for p0 in primes:
    for incr in range(1, N):
        if p0 + 2 * incr >= N:
            break
        if (p1 := p0 + incr) in primes and (p2 := p0 + 2 * incr) in primes:
            if sorted(str(p0)) == sorted(str(p1)) and sorted(str(p1)) == sorted(str(p2)):
                print(f'{p0}{p1}{p2}')
