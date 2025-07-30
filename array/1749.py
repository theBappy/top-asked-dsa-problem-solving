# kadane's algorithm
# Tc = O(n)
# Sc = O(1)
class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        maxSum = currMaxSum = nums[0]
        minSum = currMinSum = nums[0]

        for i in range(1, len(nums)):
            currMaxSum = max(nums[i], currMaxSum + nums[i])
            maxSum = max(maxSum, currMaxSum)

            currMinSum = min(nums[i], currMinSum + nums[i])
            minSum = min(minSum, currMinSum)
        return max(maxSum, abs(minSum))
