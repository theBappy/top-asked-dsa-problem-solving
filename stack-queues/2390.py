# Tc = O(n)
# Sc = O(n)


# Approach-1
class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for char in s:
            if char == '*':
                if st:
                    st.pop()
            else:
                st.append(char)
        result = ''.join(st)
        return result
    
# Approach-2
class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for char in s:
            if char == '*':
                    res.pop()
            else:
                res.append(char)
        return ''.join(res)

# Approach-3
class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)
        temp = [''] * n
        j = 0
        for i in range(n):
            if s[i] == '*':
                j -= 1  
            else:
                temp[j] = s[i]  
                j += 1  
        result = ''.join(temp[:j])
        return result