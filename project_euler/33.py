tops = []
bots = []

for top in range(11, 99):
    for bot in range(top + 1, 99):
        x0 = top / bot
        xs = []

        for idx_top in [0, 1]:
            for idx_bot in [0, 1]:
                if str(top)[idx_top] == str(bot)[idx_bot] and str(top)[idx_top] != '0' and str(bot)[1 - idx_bot] != '0':
                    xs.append(int(str(top)[1 - idx_top]) / int(str(bot)[1 - idx_bot]))

        for x in xs:
            if abs(x - x0) < 1e-5:
                tops.append(top)
                bots.append(bot)
                print(top, bot)

num = 1
denum = 1
for top, bot in zip(tops, bots):
    num *= top
    denum *= bot

print(num, denum)

div = 2
while div <= min(num, denum):
    if num % div == 0 and denum % div == 0:
        num //= div
        denum //= div
    else:
        div += 1

print(num, '=>', denum, '<=')
