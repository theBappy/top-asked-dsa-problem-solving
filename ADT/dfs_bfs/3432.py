
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        result = 0
        for i in range(n - 1):
            left_sum += nums[i]
            right_sum = total_sum - left_sum
            if (left_sum - right_sum) % 2 == 0:
                result += 1
        return result




class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        if total_sum % 2 == 0:
            return n-1
        return 0
