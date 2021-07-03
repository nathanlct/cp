"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any 
order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum
 of these four primes, 792, represents the lowest sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

with open('utils/primes_below_1e8.txt') as fp:
    primes = list(map(int, fp.read().split()))
primes_set = set(primes)
small_primes = [p for p in primes if p < 10000]

# prebuild memoiz to test if 2 primes can be concatenated into 2 new primes
memoiz = {}
def are_concatenations_primes(p0, p1):  # with p0 < p1, p0 and p1 str
    if p0 not in memoiz:
        memoiz[p0] = {}
    if p1 not in memoiz[p0]:
        memoiz[p0][p1] = int(p0 + p1) in primes_set and int(p1 + p0) in primes_set
    return memoiz[p0][p1]

def _solve(initial_primes):
    ans = []
    for p0_lst in initial_primes:
        max_p0 = p0_lst[-1][0]
        for p in small_primes:
            if p > max_p0 and p not in p0_lst:
                candidate = True
                p_str = str(p)
                for p0 in reversed(p0_lst):
                    if not are_concatenations_primes(p0[1], p_str):  # p > p0
                        candidate = False
                        break
                if candidate:
                    ans.append(p0_lst + [(p, p_str)])
    return ans

def solve(N):
    print(f'Solve for N={N}')

    # build all pairs of primes that have the property
    # then add primes to each pair to forme triples, etc recursively
    initial_primes = [[(p, str(p))] for p in small_primes]
    for p_lst in initial_primes:
        initial_primes = _solve(initial_primes)
        if len(initial_primes[0]) == N:
            break

    for p_lst in initial_primes:
        p_lst_int = [p[0] for p in  p_lst]
        print(sum(p_lst_int), p_lst_int)
    print()

# solve(4)
solve(5)
