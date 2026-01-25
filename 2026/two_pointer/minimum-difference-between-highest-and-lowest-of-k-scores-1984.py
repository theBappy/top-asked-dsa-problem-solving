class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        minDiff = float("inf")
        for i in range(k - 1, n):
            minEl = nums[i - k + 1]
            maxEl = nums[i]
            minDiff = min(minDiff, maxEl - minEl)
        return minDiff
