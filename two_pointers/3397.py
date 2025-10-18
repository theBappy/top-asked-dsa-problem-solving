class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        count = 0
        prev = float("-inf")
        for i in range(n):
            minVal = nums[i] - k
            if prev < minVal:
                prev = minVal
                count += 1
            elif prev < nums[i] + k:
                prev += 1
                count += 1
        return count
