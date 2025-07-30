
# Tc = O(n + t) [for counting freq of n ,and for t*26=t loop]
# Sc = O(n) [26 alphabets, constant space]
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        M = 10**9 + 7
        mp = [0] * 26
        
        # Count frequency of each character in the string
        for ch in s:
            mp[ord(ch) - ord('a')] += 1
        
        # Perform transformations t times
        for _ in range(t):
            temp = [0] * 26
            for i in range(26):
                freq = mp[i]
                if i < 25:  # 'a' to 'y'
                    temp[i + 1] = (temp[i + 1] + freq) % M
                else:  # 'z'
                    temp[0] = (temp[0] + freq) % M
                    temp[1] = (temp[1] + freq) % M
            mp = temp
        
        # Calculate the total length after transformations
        result = sum(mp) % M
        return result
