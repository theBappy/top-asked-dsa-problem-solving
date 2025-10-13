#  Tc = O(2 * n) => O(n) [each element visited twice using i once, j once]
#  Tc = O(1)

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        sum = 0
        i = 0
        j = 0
        while j < n:
            sum += nums[j]
            while i <= j and sum * (j - i + 1) >= k:
                sum -= nums[i]
                i += 1
            result += j - i + 1
            j += 1
        return result