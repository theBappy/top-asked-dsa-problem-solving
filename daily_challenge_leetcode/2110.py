class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        result = 1
        count = 1
        for i in range(1, len(prices)):
            if prices[i-1] - prices[i] == 1:
                count += 1
            else:
                count = 1
            result += count
        return result