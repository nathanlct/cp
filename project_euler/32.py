"""
a * b = c
a and b are < 5 digits
bc digits(c) >= max(digits(a), digits(b))
and digits(a) + digits(b) + digits(c) = 9
"""

goal = set(map(str, range(1, 10)))

ans = []
for a in range(10000):
    for b in range(a, 10000):
        c = a * b
        if len(str(a) + str(b) + str(c)) > 9:
            break
        if len(str(a) + str(b) + str(c)) != 9:
            continue
        if set(list(str(a)) + list(str(b)) + list(str(c))) == goal:
            ans.append(c)
print(sum(list(set(ans))))