# Netflix, Microsoft
# Tc = O(n)
# Sc = O(1) [not considering the result array]

class Solution:
    def getMaximumXor(self, nums, maximumBit):
        n = len(nums)
        result = [0] * n

        # step-1 : Find the total xor
        XOR = 0
        for num in nums:
            XOR ^= num

        # To find flip, first find the mask having all bits set to 1
        mask = (1 << maximumBit) - 1

        for i in range(n):
            k = XOR ^ mask  # this will give me the flipped value of XOR i.e. my best K
            result[i] = k

            XOR ^= nums[n - 1 - i]

        return result
    