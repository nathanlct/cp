n = 1
for i in range(2, 101):
    n *= i

print(sum(map(int, list(str(n)))))