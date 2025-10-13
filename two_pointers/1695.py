from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        cur_sum = 0
        start = 0 
        seen = set()
        for end in len(nums):
            while nums[end] in seen:
                seen.remove(nums[start])
                cur_sum -= nums[start]
                start += 1
            cur_sum += nums[end]
            seen.add(nums[end])
            res = max(res, cur_sum)
        return res