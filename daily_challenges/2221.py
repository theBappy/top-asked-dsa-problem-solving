
# Tc = O(n^2)
# Sc = O(n^2) [each time creating new array]
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        while len(nums) > 1:
            temp = []
            for i in range(len(nums) - 1):
                temp.append((nums[i] + nums[i + 1]) % 10)
            nums = temp
        return nums[0]

# Tc = O(n^2)
# Sc = (1)
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        for size in range(n-1, 0, -1):
            for i in range(size):
                nums[i] =( nums[i] + nums[i+1]) % 10
        return nums[0]
