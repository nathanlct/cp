

for a in range(1, 1000):
    for b in range(a+1, 1000):
        c = (a*a + b*b) ** 0.5
        if c != int(c):
            continue
        c = int(c)
        if a + b + c == 1000:
            print(a, b, c)
            print(a * b * c)
