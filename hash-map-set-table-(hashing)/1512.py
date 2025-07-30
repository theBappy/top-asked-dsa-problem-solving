# Brute Force
# Tc = O(n^2)
# Sc = O(1)
class Solution:
    def numIdenticalPairs(self, nums):
        n = len(nums)
        result = 0
        for i in range(n-1):
            num = nums[i]
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    result += 1
        return result
