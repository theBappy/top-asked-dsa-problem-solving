# 120, 165, 166, 611, 812, 976, 1039, 2221


from typing import List
def triangularSum(self, nums: List[int]) -> int:
    n = len(nums)
    for size in range(n-1, 0, -1):
        for i in range(size):
            nums[i] = (nums[i] + nums[i+1]) % 10
    return nums[0]