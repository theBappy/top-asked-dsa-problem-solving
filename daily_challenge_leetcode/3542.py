

#  Monotonic Increasing Stack
#  T.C : O(n)
#  S.C : O(n)

from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        st = []
        ops = 0
        for num in nums:
            while st and st[-1] > num:
                st.pop()
            if num == 0:
                continue
            if not st or st[-1] < num:
                st.append(num)
                ops += 1
        return ops
