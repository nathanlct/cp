from collections import defaultdict
divisors = defaultdict(list)

# compute all divisors for n <= N
N = 28123
for i in range(1, N+1):
    k = 2
    while i * k <= N:
        divisors[i * k].append(i)
        k += 1

# compute abundants numbers
abundants = []
for i in range(1, N+1):
    if sum(divisors[i]) > i:
        abundants.append(i)

# find numbers that are sum of two abundants numbers
sum_of_abundants = [False] * (N + 1)
for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        if abundants[i] + abundants[j] > N:
            break
        sum_of_abundants[abundants[i] + abundants[j]] = True

# compute sum of those who are not
ans = 0
for i, is_sum in enumerate(sum_of_abundants):
    if not is_sum:
        ans += i
print(ans)
