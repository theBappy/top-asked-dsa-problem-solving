from typing import List
class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        mp = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in mp:
                return [mp[remaining], i]
            mp[num] = i
        return []