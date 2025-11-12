from math import gcd


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count1 = nums.count(1)
        if count1 > 0:
            return n - count1
        minOps = float("inf")
        for i in range(n - 1):
            GCD = nums[i]
            for j in range(i + 1, n):
                GCD = gcd(GCD, nums[j])
                if GCD == 1:
                    minOps = min(minOps, j - i)
                    break
        if minOps == float("inf"):
            return -1
        return minOps + (n - 1)
