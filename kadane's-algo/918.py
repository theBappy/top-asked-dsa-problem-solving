class Solution(object):
    def maxSubarraySumCircular(self, A):
        total, maxSum, curMax, minSum, curMin = 0, A[0], 0, A[0], 0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
    
# brute force
def maxSubarraySumCircularBrute(nums):
    n = len(nums)
    max_sum = float('-inf')

    for start in range(n):
        # simulate rotation by slicing and concatenation
        rotated = nums[start:] + nums[:start]

        # run Kadane’s algorithm on this rotation
        curr_sum = 0
        best = float('-inf')
        for num in rotated:
            curr_sum = max(num, curr_sum + num)
            best = max(best, curr_sum)

        max_sum = max(max_sum, best)

    return max_sum
