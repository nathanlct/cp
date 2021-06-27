# 28 = 2 * 2 * 7
# a factor = multiply a certain number of each prime factor
# eg can choose from 0 to 2 "2" and from 0 to 1 "7", leaving 2*3 = 6 options, with no overlap since its primes

from collections import defaultdict

def n_divisors(N):
    if N == 1: return 1

    # get prime decomposition of N
    primes = defaultdict(int)
    p = 2
    while N > 1:
        if N % p == 0:
            primes[p] += 1
            N //= p
        else:
            p += (1 if p == 2 else 2)
    
    # get number of divisors
    ans = 1
    for count in primes.values():
        ans *= (count + 1)
    return ans


x = 1
incr = 2

while (n_div := n_divisors(x)) <= 500:
    # print(x, n_div)
    x += incr
    incr += 1

print(x)