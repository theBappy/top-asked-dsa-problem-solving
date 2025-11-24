class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        result = [False] * n
        remain = 0
        for i in range(n):
            remain = (remain * 2 + nums[i]) % 5
            result[i] = (remain == 0)
        return result