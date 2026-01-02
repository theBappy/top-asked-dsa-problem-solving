class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        st = set()
        for num in nums:
            if num in st:
                return num
            st.add(num)
        return -1

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq = [0] * 10001
        for num in nums:
            freq[num] += 1
            if freq[num] > 1:
                return num
        return -1


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(2, n):
            if nums[i] == nums[i - 1] or nums[i] == nums[i - 2]:
                return nums[i]
        return nums[-1]


