def solve(N):
    # sieve to generate all primes
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
    primes_set = set(primes)  # set for much faster "in" checking

    # precompute cumulative sum for O(1) slice summing
    primes_cumsum = [0]
    for p in primes:
        primes_cumsum.append(primes_cumsum[-1] + p)

    # look at all possible slices
    longest = 0
    argmax_longest = 0
    for i in range(len(primes_cumsum)):
        for j in range(i + 1, len(primes_cumsum)):
            slice_sum = primes_cumsum[j] - primes_cumsum[i]
            if slice_sum > N:  # break if we're over max prime, as sum will keep increasing as j increases
                break
            if slice_sum in primes_set:
                if j - i > longest:
                    longest = j - i
                    argmax_longest = slice_sum

    print(longest, argmax_longest)
    return argmax_longest


print('=>', solve(100))
print('=>', solve(1000))
print('=>', solve(int(1e6)))