
from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i+1] = 0
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        while j < n:
            nums[j] = 0
            j += 1
        return nums 




class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        j = 0
        for i in range(n):
            if i + 1 < n and nums[i] == nums[i+1] and nums[i] != 0:
                nums[i] *= 2
                nums[i + 1] = 0
            if nums[i] != 0:
                if i != j:
                    nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums
    

        
    

