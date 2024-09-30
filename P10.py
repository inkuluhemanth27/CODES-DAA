def minCoins(coins, sum):
    dp = [float('inf')] * (sum + 1)
    dp[0] = 0 
    for coin in coins:
        for x in range(coin, sum + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[sum] if dp[sum] != float('inf') else -1
coins = [1, 2, 5]
sum = 11
print(minCoins(coins, sum)) 
