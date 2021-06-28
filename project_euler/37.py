N = int(1e6)

sieve = [True] * N
sieve[0] = False
sieve[1] = False
for i in range(2, N):
    if sieve[i]:
        k = 2
        while (prod := i * k) < N:
            sieve[prod] = False
            k += 1

ans = []
count = 0
for i in range(11, N):
    if sieve[i]:
        si = str(i)
        candidate = True
        for k in range(1, len(si)):
            if not sieve[int(si[:k])] or not sieve[int(si[k:])]:
                candidate = False
        if candidate:
            count += 1
            ans.append(i)
            print(i)

assert(count == 11)
print('ans', sum(ans))