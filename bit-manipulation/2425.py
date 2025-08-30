# Meta, Tiktok

# Tc = O(n)
# Sc = O(n) [for map]
from collections import defaultdict
class Solution:
    def xorAllNums(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        mp = defaultdict(int)
        for num in nums1:
            mp[num] += n
        for num in nums2:
            mp[num] += m
        result = 0
        for num, freq in mp.items():
            if freq % 2 != 0:
                result ^= num

        return result
    

# if nums1.length = odd, nums2 will stay
# if nums2.length = odd, nums1 will stay
# and both length equal result will be 0
class Solution:
    def xorAllNums(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)

        XOR = 0
        if m % 2 != 0:
            for num in nums2:
                XOR ^= num

        if n % 2 != 0:
            for num in nums1:
                XOR ^= num
        return XOR