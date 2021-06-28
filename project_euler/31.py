coins = [1, 2, 5, 10, 20, 50, 100, 200]

# no memoiz
def solve_recursion(goal=200, max_coin=200):
    if goal == 0:
        return 1
    ans = 0
    for coin in coins:
        if coin <= goal and coin <= max_coin:
            ans += solve_recursion(goal - coin, max_coin=coin)
    return ans

def solve_dp(goal=200):
    dp = [[0] * len(coins) for _ in range(goal + 1)]
    # dp[i][j] = nb of ways for goal=i using coins 0 to j

    for i in range(goal + 1):
        for j in range(len(coins)):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + (dp[i - coins[j]][j] if i - coins[j] >= 0 else 0)
    
    return dp[-1][-1]

print(solve_recursion())
print(solve_dp())