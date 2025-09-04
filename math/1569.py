# Google
# Tc = O(n^2)
# Sc = O(n^2)

from typing import List
class Solution:
    MOD = 10**9 + 7
    def numOfWays(self, nums: List[int]) -> int:
        n = len(nums)
        # Precompute Pascal's triangle for binomial coefficients
        self.PT = [[1] * (i + 1) for i in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, i):
                self.PT[i][j] = (self.PT[i - 1][j - 1] + self.PT[i - 1][j]) % self.MOD
        def solve(arr: List[int]) -> int:
            m = len(arr)
            if m < 3:
                return 1
            root = arr[0]
            left_array = [x for x in arr[1:] if x < root]
            right_array = [x for x in arr[1:] if x >= root]
            left_ways = solve(left_array) % self.MOD
            right_ways = solve(right_array) % self.MOD
            ways_to_interleave = self.PT[m - 1][len(left_array)]
            return (left_ways * right_ways * ways_to_interleave) % self.MOD
        # Subtract 1 because the problem usually asks for ways excluding the original order
        return (solve(nums) - 1) % self.MOD