class Solution:
    def isIncreasing(self, nums: List[int], s: int, e: int) -> bool:
        for i in range(s + 1, e):
            if nums[i] <= nums[i - 1]:
                return False
        return True

    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for start in range(n - 2 * k + 1):
            first = self.isIncreasing(nums, start, start + k)
            second = self.isIncreasing(nums, start + k, start + 2 * k)
            if first and second:
                return True
        return False
    

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        currRun = 1
        prevRun = 0
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                currRun += 1
            else:
                prevRun = currRun
                currRun = 1
            if currRun >= 2*k:
                return True
            elif min(currRun, prevRun) >= k:
                return True
        return False
