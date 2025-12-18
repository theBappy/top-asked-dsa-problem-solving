class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        actualProfit = 0
        profit = [0] * n

        for i in range(n):
            profit[i] = strategy[i] * prices[i]
            actualProfit += profit[i]

        originalWindowProfit = 0
        modifiedWindowProfit = 0
        maxGain = 0

        i = 0
        j = 0

        while j < n:
            originalWindowProfit += profit[j]

            if j - i + 1 > k // 2:
                modifiedWindowProfit += prices[j]

            if j - i + 1 > k:
                originalWindowProfit -= profit[i]
                modifiedWindowProfit -= prices[i + k // 2]
                i += 1

            if j - i + 1 == k:
                maxGain = max(maxGain, modifiedWindowProfit - originalWindowProfit)

            j += 1

        return actualProfit + maxGain
