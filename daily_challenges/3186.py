
# Tc = O(n.logn)
# Sc = O(n)

from bisect import bisect_left
from collections import Counter

class Solution:
    def __init__(self):
        self.mp = {}
        self.t = []
        self.n = 0

    def solve(self, i, nums):
        if i >= self.n:
            return 0

        if self.t[i] != -1:
            return self.t[i]

        # skip current damage
        skip = self.solve(i + 1, nums)

        # take current damage
        j = bisect_left(nums, nums[i] + 3, i + 1)
        take = nums[i] * self.mp[nums[i]] + self.solve(j, nums)

        self.t[i] = max(skip, take)
        return self.t[i]

    def maximumTotalDamage(self, power):
        self.mp = Counter(power)
        nums = sorted(self.mp.keys())
        self.n = len(nums)
        self.t = [-1] * self.n

        return self.solve(0, nums)