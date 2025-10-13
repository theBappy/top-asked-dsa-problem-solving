

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        product = 1
        i = 0
        j = 0
        while j < n:
            product *= nums[j]
            while i <= j and product >= k:
                product /= nums[i]
                i += 1
            result += j - i + 1
            j += 1
        return result
