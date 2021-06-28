def solve(N):
    ans = 1
    count = 1
    for i in range(N // 2):
        increment = (i + 1) * 2
        for _ in range(4):
            count += increment
            ans += count
    return ans

print(solve(5))
print(solve(1001))