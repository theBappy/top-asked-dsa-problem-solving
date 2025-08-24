# Google, Meta, Apple
# Best time to buy and sell stock with transaction fee
# Recursion + Memoization
# Transaction fee = Sell - Buy [at the time of just selling needs transaction fee][must sell the stock before buy again]

# Tc = O(n)
# Sc = O(1)

class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        if n == 0:
            return 0

        # Initialize variables to store the maximum profit
        cash = 0  # Maximum profit when not holding a stock
        hold = -prices[0]  # Maximum profit when holding a stock

        for i in range(1, n):
            # Update cash and hold for the current day
            cash = max(cash, hold + prices[i] - fee)  # Sell stock
            hold = max(hold, cash - prices[i])  # Buy stock

        return cash  # Maximum profit at the end of the last day