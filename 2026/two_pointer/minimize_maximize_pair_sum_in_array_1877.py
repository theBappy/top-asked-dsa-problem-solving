class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_result = 0
        i, j = 0, len(nums) - 1
        while i < j:
            sum_pair = nums[i] + nums[j]
            max_result = max(max_result, sum_pair)
            i += 1
            j -= 1
        return max_result
