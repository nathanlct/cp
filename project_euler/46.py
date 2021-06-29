N = int(1e5)

sieve = [True] * N
sieve[0] = False
sieve[1] = False
for i in range(2, N):
    if sieve[i]:
        k = 2
        while (prod := i * k) < N:
            sieve[prod] = False
            k += 1

primes = [i for i, v in enumerate(sieve) if v]
two_squares = [2 * i * i for i in range(int(N ** 0.5))]

new_sieve = [False] * (max(primes) + max(two_squares) + 1)

for prime in primes:
    for two_square in two_squares:
        new_sieve[prime + two_square] = True

for i, v in enumerate(new_sieve):
    if i >= 2 and i % 2 == 1:
        if not v:
            print(i)
            break
