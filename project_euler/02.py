ans = 0

a, b = 1, 2
while a < 4e6:
    if a % 2 == 0:
        ans += a
    a, b = b, a + b

print(ans)