class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        minSum = float("inf")
        index = 1
        for i in range(len(nums) - 1):
            if nums[i] + nums[i + 1] < minSum:
                index = i
                minSum = nums[i] + nums[i + 1]
        return index

    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0
        while nums != sorted(nums):
            index = self.minPairSum(nums)
            nums[index] = nums[index] + nums[index + 1]
            nums.pop(index + 1)
            operations += 1
        return operations
