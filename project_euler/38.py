ans = []

for n in range(2, 9):
    for x in range(int(10 ** (10 // n))):
        s = ''
        for i in range(1, n+1):
            s += str(i * x)
        if len(s) > 9:
            break
        if len(s) < 9:
            continue
        if set(list(s)) == set(list('123456789')):
            print(x, n)
            ans.append(int(s))

print('ans', max(ans))
