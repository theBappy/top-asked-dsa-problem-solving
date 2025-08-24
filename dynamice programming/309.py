# Google, Microsoft, Meta, Amazon
# Cool-down: if buy in i'th day, then (i+1)'th day can not buy, have to relax this day
# Tc = O(n)
# Sc = O(n)

class Solution:
    def __init__(self):
        self.t = [[-1 for _ in range(2)] for _ in range(5001)]

    def solve(self, prices, day, n, buy):
        if day >= n:
            return 0
        if self.t[day][buy] != -1:
            return self.t[day][buy]
        
        profit = 0
        if buy:
            selling_day = self.solve(prices, day + 1, n, False) - prices[day]  # selling - bought_price
            buying_day = self.solve(prices, day + 1, n, True)  # buying only
            profit = max(profit, selling_day, buying_day)
        else:
            buying_day = prices[day] + self.solve(prices, day + 2, n, True)
            selling_day = self.solve(prices, day + 1, n, False)
            profit = max(profit, buying_day, selling_day)
        
        self.t[day][buy] = profit
        return profit

    def maxProfit(self, prices):
        n = len(prices)
        return self.solve(prices, 0, n, True)  # first day need to buy for having stock
    

# Bottom up 
# State definition: t[i] = max total profit until day i
# profit = prices[i] - prices[j] -> (sell - buy)
# t[i] = profit + prevProfit