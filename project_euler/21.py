from collections import defaultdict
divisors = defaultdict(list)

# compute all divisors for n <= N
N = 10000
for i in range(1, N+1):
    k = 2
    while i * k <= N:
        divisors[i * k].append(i)
        k += 1

# find amicable pairs
ans = 0
for a in range(1, N+1):
    b = sum(divisors[a])
    if a != b and sum(divisors[b]) == a:
        ans += a

print(ans)