class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        lastOne = -(k + 1)
        for i in range(n):
            if nums[i] == 1:
                if i - lastOne - 1 < k:
                    return False
                lastOne = i
        return True
