# Amazon, Google, Meta, Apple, Netflix
# Arithmetic sub-sequence: At least 3 elements that form an arithmetic progression
# Tc = O(n^2)
# Sc = O(n.d) [d = number of distinct difference, in worst case it could be n so Tc is O(n^2)]

from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        result = 0
        mp = [defaultdict(int) for _ in range(n)] # for each i, store {diff : count}
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                count_at_j = mp[j][diff]
                
                mp[i][diff] += count_at_j + 1
                
                result += count_at_j
        
        return result
