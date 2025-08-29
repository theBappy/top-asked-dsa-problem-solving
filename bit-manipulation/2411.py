# Netflix, Microsoft

# Tc = O(n)
# Sc = O(1)

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        setBitIndex = [-1] * 32 # Sc = O(32) => O(1)

        for i in range(n-1, -1, -1): #O(n)
            endIndex = i
            for j in range(32): #O(32) => O(1)
                if not(nums[i] & (1 << j)):
                    if setBitIndex[j] != -1:
                        endIndex = max(endIndex, setBitIndex[j])
                else:
                    setBitIndex[j] = i

            result[i] = endIndex - i + 1
        return result