#You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

# Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.

# You may assume that you have an unlimited number of each coin.

def coin_change(coins, amount):
    # Initialize a list to store the minimum coins needed for each amount
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make amount 0

    # Iterate through each amount from 1 to amount
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
        
    return dp[amount] if dp[amount]!= float('inf') else -1