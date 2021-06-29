def solve(N):
    s = 0
    for i in range(1, N+1):
        s += i ** i
    return s

print(solve(10))
print(str(solve(1000))[-10:])