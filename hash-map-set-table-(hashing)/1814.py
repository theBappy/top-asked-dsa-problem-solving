
# Tc = O(n * logn) + O(n) [n for processing the loop of nums[i] and rev can take logn] and the resulting loops O(n) thus the dominate O(n * logn)
# Sc = O(n) for the hash map
class Solution:
    def rev(self, num):
        ans = 0
        while num > 0:
            remainder = num % 10
            ans = (ans * 10) + remainder
            num //= 10
        return ans

    def countNicePairs(self, nums):
        M = 10**9 + 7
        n = len(nums)
        mp = {}
        for i in range(n):
            nums[i] = nums[i] - self.rev(nums[i]) 
        result = 0
        for i in range(n):
            result = (result + mp.get(nums[i], 0)) % M
            mp[nums[i]] = mp.get(nums[i], 0) + 1
        return result


        
    