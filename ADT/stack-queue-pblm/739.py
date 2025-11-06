# Google, Meta
# Monotonic Stack => maintaining a order (increasing or decreasing order)
# In Stack, Each element only push once or pop once, never push or pop more than one, only twice works push + pop => O(n * 2) => O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
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
