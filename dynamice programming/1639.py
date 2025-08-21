# Google, Amazon

# Number of ways to form a string
# Same index cannot be used again in another word suppose if index is 1 then 0, 1 of each word index cannot use again..left to used index will be forbidden to use again for other words too

# T.C : O(n*k + m*k)
# S.C : O(m*k)

from typing import List
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m = len(target)
        k = len(words[0])
        MOD = 10**9 + 7
        
        # Frequency array
        freq = [[0] * k for _ in range(26)]
        
        # Fill frequency array
        for col in range(k):
            for word in words:
                ch = word[col]
                freq[ord(ch) - ord('a')][col] += 1
        
        # Memoization table
        t = [[-1] * (k + 1) for _ in range(m + 1)]
        
        def solve(i, j):
            if i == m:
                return 1
            if j == k:
                return 0
            if t[i][j] != -1:
                return t[i][j]
            
            not_taken = solve(i, j + 1) % MOD
            taken = (freq[ord(target[i]) - ord('a')][j] * solve(i + 1, j + 1)) % MOD
            
            t[i][j] = (not_taken + taken) % MOD
            return t[i][j]
        
        return solve(0, 0)

