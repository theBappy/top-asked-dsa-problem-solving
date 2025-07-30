# Tc = O(n)
# Sc = O(n)
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        st = []
        result = [0] * n
        
        for i in range(n - 1, -1, -1):
            while st and temperatures[i] >= temperatures[st[-1]]:
                st.pop()
            if not st:
                result[i] = 0
            else:
                result[i] = st[-1] - i
            st.append(i)
        
        return result

