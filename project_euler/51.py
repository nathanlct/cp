"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, 
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

def sieve_eratosthenes(limit, return_primes=True):
    arr = [False, False] + [True] * (limit - 1)
    for n in range(2, int(limit ** 0.5) + 1):
        if arr[n]:
            for k in range(2, limit // n + 1):
                arr[k * n] = False
    if return_primes:
        return [n for n, is_prime in enumerate(arr) if is_prime]
    return arr

def solve(N):
    primes = sieve_eratosthenes(1000000)
    primes_set = set(primes)

    for prime in primes:
        prime_str = str(prime)
        for digit in set(list(prime_str)):
            replacements = [prime_str.replace(digit, new_digit) for new_digit in '0123456789']
            prime_replacements = [n for n in replacements if int(n) in primes_set and n[0] != '0'] 
            if len(prime_replacements) >= N:
                print(prime, digit, prime_replacements)
                return 

solve(6)
solve(7)
solve(8)