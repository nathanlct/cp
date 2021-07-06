def nth_prime(N):
    k = 2
    primes = [k]
    n = 1
    while n < N:
        # find next prime
        search = True
        while search:
            k += (1 if k == 2 else 2)
            search = False
            for p in primes:
                if p > k ** 0.5:  # essential
                    break
                if k % p == 0:
                    search = True
                    break
        primes.append(k)
        n += 1        
    return primes[-1]

print(nth_prime(6))
print(nth_prime(10001))
