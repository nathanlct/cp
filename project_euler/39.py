max_sols = 0
argmax_sols = 0

for p in range(1001):
    print(p)
    sols = 0
    for a in range(1, p // 3):
        for b in range(a, p // 2):
            c = p - a - b
            if (c := p - a - b) >= b:
                if a * a + b * b == c * c:
                    sols += 1
            else:
                break
    if sols > max_sols:
        max_sols = sols
        argmax_sols = p

print(argmax_sols, max_sols)
