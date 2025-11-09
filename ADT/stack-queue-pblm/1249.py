

# Tc = O(n)
# Sc = O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        st = []
        remove_idx = set()
        for i in range(n):
            if s[i] == "(":
                st.append(i)
            elif s[i] == ")":
                if not st:
                    remove_idx.add(i)
                else:
                    st.pop()

        while st:
            remove_idx.add(st.pop())
        result = []
        for i in range(n):
            if i not in remove_idx:
                result.append(s[i])
        return result
