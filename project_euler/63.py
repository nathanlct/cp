power = 1
ans = 0

while True:
    number = 1
    
    while True:
        digits = len(str(number ** power))
        if digits > power:
            break
        if digits == power:
            print(number ** power)
            ans += 1
        number += 1

    power += 1
    if power > 500:
        break

print('ans', ans)