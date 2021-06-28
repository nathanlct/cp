def solve(N):
    sieve = [True] * N
    sieve[0] = False
    sieve[1] = False
    for i in range(2, N):
        if sieve[i]:
            k = 2
            while (prod := i * k) < N:
                sieve[prod] = False
                k += 1
    
    ans = 0
    for i in range(2, N):
        if sieve[i]:
            si = str(i)
            candidate = True
            for _ in range(len(si) - 1):
                si = si[1:] + si[0]
                if not sieve[int(si)]:
                    candidate = False
                    break
            if candidate:
                ans += 1

    return ans

print(solve(100))
print(solve(int(1e6)))