from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        swap_index = -1
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                swap_index = i - 1
                break
        if swap_index != -1:
            just_greater = swap_index
            for j in range(n-1, swap_index, -1):
                if nums[j] > nums[swap_index]:
                    just_greater = j
                    break
            nums[swap_index], nums[just_greater] = nums[just_greater], nums[swap_index]
        nums[swap_index+1:] = reversed(nums[swap_index+1:])
