# Tc = O(n) [each element visiting twice only]
# Sc = O(n)

from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums):
        n = len(nums)
        unique_elements = set(nums)
        c = len(unique_elements)
        i = 0
        j = 0
        res = 0
        mp = defaultdict(int)
        while j < n:
            mp[nums[j]] += 1
            while len(mp) == c:
                res += (n - j)
                mp[nums[i]] -= 1
                if mp[nums[i]] == 0:
                    del mp[nums[i]]
                i += 1
            j += 1
        return res