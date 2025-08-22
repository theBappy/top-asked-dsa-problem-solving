# Google
# Tc = O(m * n * log(n))
# Sc = O(m * n) [memoization for (idx, prev) unique states]

from bisect import bisect_right
from collections import defaultdict

class Solution:
    def __init__(self):
        self.mp = defaultdict(int)

    def solve(self, idx, arr1, arr2, prev):
        if idx == len(arr1):
            return 0
        if (idx, prev) in self.mp:
            return self.mp[(idx, prev)]
        
        result1 = float('inf')
        if arr1[idx] > prev:
            result1 = self.solve(idx + 1, arr1, arr2, arr1[idx])
        result2 = float('inf')
        i = bisect_right(arr2, prev) # in arr2 just prev element than idx
        if i < len(arr2):
            result2 = 1 + self.solve(idx+1, arr1, arr2, arr2[i])
        self.mp[(idx, prev)] = min(result1, result2)
        return self.mp[(idx, prev)]

    def makeArrayIncreasing(self, arr1, arr2):
        arr2.sort()
        self.mp.clear()
        result = self.solve(0, arr1, arr2, float('inf'))
        return -1 if result == float('inf') else result