def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return (n == 2)
    for k in range(3, int(n ** 0.5) + 1, 2):
        if n % k == 0: return False
    return True


counter = 1
incr = 2

n_primes = 0

while True:
    for _ in range(4):
        counter += incr
        if is_prime(counter):
            n_primes += 1

    ratio = n_primes / (1 + 2 * incr)
    if ratio < 0.1:
        print(incr + 1)
        break        
    
    incr += 2