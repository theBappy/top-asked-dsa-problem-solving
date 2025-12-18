# What is short selling?

# Can reduce price value if someone can guess it, so he borrow some and immediately sell it.
# when near feture when the same product price is less than he previously bought, so he will buy
# But in real world have risks too

# Buy -> Sell
# Sell -> Buy (short selling)

from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        INF = int(1e18)  # safe sentinel for long long
        
        # 3D DP table: dp[i][k][CASE]
        # i -> current day
        # k -> remaining transactions
        # CASE -> 0: can buy/sell, 1: must buy, 2: must sell
        dp = [[[-INF] * 3 for _ in range(k+1)] for _ in range(n)]
        
        def solve(i: int, k_remain: int, CASE: int) -> int:
            # Base case: reached end of prices array
            if i == n:
                if CASE == 0:
                    return 0
                return -INF
            
            # Memoization check
            if dp[i][k_remain][CASE] != -INF:
                return dp[i][k_remain][CASE]
            
            # Skip today
            skip = solve(i + 1, k_remain, CASE)
            take = -INF  # profit if we take an action today
            
            if k_remain > 0:
                if CASE == 1:
                    # Must sell today
                    take = prices[i] + solve(i + 1, k_remain - 1, 0)
                elif CASE == 2:
                    # Must buy today
                    take = -prices[i] + solve(i + 1, k_remain - 1, 0)
                else:
                    # Can choose to buy or sell
                    take = max(
                        -prices[i] + solve(i + 1, k_remain, 1),  # buy
                        prices[i] + solve(i + 1, k_remain, 2)    # sell
                    )
            
            # Memoize and return
            dp[i][k_remain][CASE] = max(skip, take)
            return dp[i][k_remain][CASE]
        
        return solve(0, k, 0)

# Example usage:
# sol = Solution()
# print(sol.maximumProfit([3,2,6,5,0,3], 2))  # Output: maximum profit
