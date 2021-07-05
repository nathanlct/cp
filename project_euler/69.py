from collections import defaultdict

def solve(N):
    # sieve-style, compute prime decomposition of each n <= N
    decomps = []
    for _ in range(N + 1):
        decomps.append(defaultdict(int))
    for n in range(2, N + 1):
        if all([v == 0 for v in decomps[n].values()]):  # if n is prime
            decomps[n][n] = 1
            for k in range(2, N // n + 1):
                decomps[k * n][n] += 1 + decomps[k][n]

    # phi(p1^k1...pi^ki...) = prod_i (pi-1)pi^{ki-1}
    max_nphi = 0
    argmax_nphi = -1
    for n, decomp in enumerate(decomps):
        phi = 1
        for p, k in decomp.items():
            if k > 0:
                phi *= (p - 1) * (p ** (k - 1))
        if n / phi > max_nphi:
            max_nphi = n / phi
            argmax_nphi = n

    return argmax_nphi

print(solve(int(10)))
print(solve(int(1e6)))
