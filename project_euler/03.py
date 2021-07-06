def prime_factors(N):
    factors = []
    p = 2
    while N > 1:
        if N % p == 0:
            factors.append(p)
            N //= p
        else:
            if p == 2: p += 1
            else: p += 2
    return factors

print(prime_factors(13195))
print(max(prime_factors(600851475143)))