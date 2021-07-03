"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any 
order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum
 of these four primes, 792, represents the lowest sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

# load all primes below 1e8 (generated with sieve)
with open('utils/primes_below_1e8.txt') as fp:
    primes = list(map(int, fp.read().split()))

# turn into set for O(1) prime checking
primes_set = set(primes)


def solve(N, max_prime):
    print(f'\nSolve for N={N}')

    # get primes we're interested in testing
    small_primes = [p for p in primes if p < max_prime]

    # prebuild table to test if 2 primes can be concatenated into 2 new primes
    are_concats_primes = {}
    for i in range(len(small_primes)):
        are_concats_primes[i] = {}
        for j in range(i + 1, len(small_primes)):
            are_concats_primes[i][j] = int(str(small_primes[i]) + str(small_primes[j])) in primes_set \
                                and int(str(small_primes[j]) + str(small_primes[i])) in primes_set

    # iteratively build all lists of primes with the property, of length 1, then 2, then ..., then N
    candidates = [[i] for i in range(len(small_primes))]
    for _ in range(N - 1):
        new_candidates = []
        for idx_lst in candidates:
            for new_idx in range(idx_lst[-1] + 1, len(small_primes)):
                if all([are_concats_primes[idx][new_idx] for idx in idx_lst]):
                    new_candidates.append(idx_lst + [new_idx])
        candidates = new_candidates

    # print results
    for sol in candidates:
        p_lst = [small_primes[i] for i in sol]
        print(sum(p_lst), p_lst)

# solve
solve(N=4, max_prime=1000)
solve(N=5, max_prime=10000)
