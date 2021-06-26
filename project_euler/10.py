def sum_primes(upper):
    sieve = { k: True for k in range(2, upper) }
    i = 2
    ans = 0
    while i < upper:
        if sieve[i]:
            ans += i
            k = 2 * i 
            while k < upper:
                sieve[k] = False
                k += i
        i += 1
    return ans

print(sum_primes(10))
print(sum_primes(int(2e6)))