# Meta, Amazon
# Monotonic Stack (Increasing or Decreasing order)

# Tc = O(n)
# Sc = O(n) [stack]
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        num3 = float("-inf")
        st = []
        for i in range(n - 1, -1, -1):
            if nums[i] < num3:
                return True
            while st and st[-1] < nums[i]:
                num3 = st.pop()
            st.append(nums[i])
        return False

