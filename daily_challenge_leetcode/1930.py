# Tc = O(n)
# Sc = O(1)
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        unique_letters = set(s)
        result = 0
        for letter in unique_letters: # Tc = O(26) -> lower english letters
            first_idx = -1
            last_idx = -1
            for i in range(n): # O(n)
                if s[i] == letter:
                    if first_idx == -1:
                        first_idx = i
                    last_idx = i
            st = set()
            for middle in range(first_idx + 1, last_idx): #O(26 * n)
                st.add(s[middle])
            result += len(st)
        return result
