# Tc = O(n)
# Sc = O(n)
from collections import defaultdict
from typing import List
class Solution:
    def subArraySum(self, nums: List[int], k:int) -> int:
        res = 0
        curSum = 0
        prefixSums = { 0 : 1 }
        for n in nums:
            curSum += n
            diff = curSum - k
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(diff, 0)
        return res
