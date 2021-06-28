idx = list(map(int, [1, 10, 1e2, 1e3, 1e4, 1e5, 1e6]))

s = ''
i = 1
while len(s) < max(idx):
    s += str(i)
    i += 1

ans = 1
for i in idx:
    ans *= int(s[i-1])

print(ans)