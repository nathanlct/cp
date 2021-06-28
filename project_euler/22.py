with open('22.txt', 'r') as fp:
    data = fp.read()

names = data.split(',')
names = sorted([name[1:-1] for name in names])

ans = 0
for i, name in enumerate(names):
    score = 0
    for c in name:
        score += ord(c) - ord('A') + 1
    score *= i + 1
    ans += score
print(ans)
