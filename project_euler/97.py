a = 28433
b = 7830457

x = a
for i in range(b):
    if i % 100 == 0:
        x = int(str(x)[-10:])
    x *= 2
x += 1

print(str(x)[-10:])