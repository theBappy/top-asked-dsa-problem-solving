class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pair_idx = {}
        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target-num]]
            pair_idx[num] = i

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapping = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mapping:
                return [mapping[diff], i]
            else:
                mapping[nums[i]] = i