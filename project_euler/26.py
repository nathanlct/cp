"""
1/6

1/6 = 0 remainder 1
add .0 remainder 10
10/6 = 1 remainder 4
add 0 remainder 40
40/6 = 6 remainder 4 <- loop

finite number of remainders bc rational number
so it either ends with a remainder 0, or loops
"""


def one_over(bot):
    """
    Returns fixed_part, repeating_part where 1/bot = 0.fixed_part(repeating_part)
    """
    assert (bot == int(bot) and bot > 1)
    ans = ''
    remainder = 1
    i = 0
    seen_remainder = {remainder: i}
    while True:
        i += 1
        remainder *= 10
        new_digit, remainder = remainder // bot, remainder % bot
        ans += str(new_digit)

        if remainder == 0:
            return ans, ''

        if remainder in seen_remainder:
            idx = seen_remainder[remainder]
            return ans[:idx], ans[idx:]

        seen_remainder[remainder] = i

max_cycle = 0
argmax_cycle = 0
for i in range(2, 1000):
    res = one_over(i)
    if len(res[1]) > max_cycle:
        max_cycle = len(res[1])
        argmax_cycle = i
print(argmax_cycle, one_over(argmax_cycle))