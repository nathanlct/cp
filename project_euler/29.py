def solve(N):
    terms = set()
    for a in range(2, N+1):
        for b in range(2, N+1):
            terms.add(a ** b)
    return len(terms)

print(solve(5))
print(solve(100))