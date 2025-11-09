#  using stack
#  Tc = O(n)
#  Sc = O(n)
class Solution:
    def minSwaps(self, s: str) -> int:
        st = []
        for ch in s:
            if ch == "[":
                st.append(ch)
            elif st:
                st.pop()
        return (len(st) + 1) // 2


# without using stack
#  Tc = O(n)
#  Sc = O(1)
class Solution:
    def minSwaps(self, s: str) -> int:
        size = 0
        for ch in s:
            if ch == "[":
                size += 1
            elif size != 0:
                size -= 1
        return (size + 1) // 2
