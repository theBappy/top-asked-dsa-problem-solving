# 120, 165, 166, 611

from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        count = 0
        for k in range(n-1, -1, -1):
            i, j = 0, k-1
            while i < j:
                if nums[i]+nums[j] > nums[k]:
                    count += (j-1)
                    j -= 1
                else:
                    i += 1
        return count
