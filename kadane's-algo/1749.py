# Tc = O(n)
# Sc = O(1)

from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)

        maxSum = nums[0]
        minSum = nums[0]

        currSumMax = nums[0]
        currSumMin = nums[0]

        for i in range(1, n):
            currSumMax = max(nums[i], currSumMax + nums[i])
            maxSum = max(maxSum, currSumMax)

            currSumMin = min(nums[i], currSumMin + nums[i])
            minSum = min(minSum, currSumMin)

        return max(maxSum, abs(minSum))