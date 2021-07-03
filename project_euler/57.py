"""
1 + top_i/bot_i
1 + top_{i+1}/bot_{i+1} = 1 + 1/(2+top_i/bot_i)
                        = 1 + bot_i/(2*bot_i + top_i)
    => top_{i+1} = bot_i
       bot_{i+1} = 2 * bot_i + top_i

frac = 1 + top/bot = (bot + top) / bot
"""

ans = 0

top = 1
bot = 2
for k in range(1000):
    frac = (bot + top, bot)
    top, bot = bot, 2 * bot + top

    if len(str(frac[0])) > len(str(frac[1])):
        ans += 1

print(ans)