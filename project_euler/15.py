def n_roads(N):
    # NxN grid
    # theres N horizontals and N verticals, we only need to place horizontals
    # ie binomial coef, choose N elements among 2N
    ans = 1
    # count number of ways of placing horizontals
    for k in range(2 * N, N, -1):
        ans *= k
    # remove ways that are the same but in a different order
    for k in range(N, 0, -1):
        ans //= k
    return ans

print(n_roads(2))
print(n_roads(20))