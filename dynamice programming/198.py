# Google, Amazon, AirBnB, OYO, Microsoft
# Stickler Thief
# Why DP?
# We have options to choose
# Find Optimal (max/min)
# Overlapping Sub-problems

# Recursion + Memoization (Top-Down)
# Tc, Sc = O(n)
class Solution:
    def __init__(self):
        self.t = [-1] * 101

    def solve(self, nums, i, n):
        if i >= n:
            return 0
        if self.t[i] != -1:
            return self.t[i]
        steal = nums[i] + self.solve(nums, i + 2, n)
        skip = self.solve(nums, i + 1, n)
        self.t[i] = max(steal, skip)
        return self.t[i]

    def rob(self, nums):
        n = len(nums)
        self.t = [-1] * 101
        return self.solve(nums, 0, n)
    
# Bottom-Up Approach
# Define-> t[i] = max stolen money till house i
class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # Initialize the memoization array
        t = [0] * (n + 1)
        
        # Base cases
        t[0] = 0  # No house, no money
        t[1] = nums[0]  # Only one house
        
        for i in range(2, n + 1):
            steal = nums[i - 1] + t[i - 2]  # Money if we rob the current house
            skip = t[i - 1]  # Money if we skip the current house
            t[i] = max(steal, skip)  # Max money we can have up to house i
        
        return t[n]  # Return the maximum money that can be robbed


