# Google, Meta
# Recur + Memo
# Tc = O(n * k) [combination of pile index and remaining coins]
# Sc = O(n * k) also recursion stack can goes as deep as n but this is dominated by memoization table

from typing import List
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        t = [[-1] * (k + 1) for _ in range(n + 1)]

        def solve(i, k):
            if i >= n:
                return 0
            if t[i][k] != -1:
                return t[i][k]
            
            not_taken = solve(i + 1, k)
            taken = 0
            sum_coins = 0
            
            for j in range(min(len(piles[i]), k)):
                sum_coins += piles[i][j]
                if j + 1 <= k:  # Ensure we do not exceed k
                    taken = max(taken, sum_coins + solve(i + 1, k - (j + 1)))
            
            t[i][k] = max(taken, not_taken)
            return t[i][k]

        return solve(0, k)



# Bottom up approach
# State define: t[i][j] = max value when you have 'i' piles and can take at most j coins from the i pile
# need to return t[n][k]
# Tc = O(n.k.m)
# Sc = O(n.k) [due to 2D array]

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        t = [[0] * (k + 1) for _ in range(n + 1)]

        for pile in range(1, n + 1):
            for coins in range(k + 1):
                sum_coins = 0
                for curr_coin in range(min(len(piles[pile - 1]), coins) + 1):
                    if curr_coin > 0:
                        sum_coins += piles[pile - 1][curr_coin - 1]
                    t[pile][coins] = max(
                        t[pile][coins], sum_coins + t[pile - 1][coins - curr_coin]
                    )

        return t[n][k]




