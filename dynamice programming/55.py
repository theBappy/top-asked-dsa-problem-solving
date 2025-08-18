# Microsoft, Abode
# Tc = O(n)
class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        maxReachable = 0
        for i in range(n):
            if i > maxReachable:
                return False
            maxReachable = max(maxReachable, i + nums[i])
        return True
        