# Meta, Google

# Tc = O(n)
# Sc = O(n)
# Recursion + Memoization

class Solution(object):
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        t = [-1] * (n + 1)

        def solve(i):
            if i == n:
                return 0
            
            if t[i] != -1:
                return t[i]
            
            t[i] = stoneValue[i] - solve(i + 1)
            
            if i + 1 < n:
                t[i] = max(t[i], stoneValue[i] + stoneValue[i + 1] - solve(i + 2))
            
            if i + 2 < n:
                t[i] = max(t[i], stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - solve(i + 3))
            
            return t[i]

        diff = solve(0)

        if diff < 0:
            return "Bob"
        elif diff > 0:
            return "Alice"
        
        return "Tie"