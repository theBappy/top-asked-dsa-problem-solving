class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        n = len(pushed)
        i = 0
        j = 0
        while i < n and j < n:
            st.append(pushed[i])
            while st and j < n and st[-1] == popped[j]:
                st.pop()
                j += 1
            i += 1
        return not st
