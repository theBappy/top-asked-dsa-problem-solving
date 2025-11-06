class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for i in range(len(s) - 1, -1, -1):
            if not st or st[-1] != s[i]:
                st.append(s[i])
            else:
                st.pop()
        result = ""
        while st:
            result += st.pop()
        return result
