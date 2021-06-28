
i = 1
a, b = 1, 1
N = 1000

while True:
    if len(str(a)) == N:
        print(i, a)
        break
    a, b = b, a + b
    i += 1