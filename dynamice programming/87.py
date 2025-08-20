# Google
# MCM -> Matrix Chain Multiplication
# Scramble String
# Recur + Memo

# Tc = O(n^4)
# Sc = O(n^2)

class Solution:
    def __init__(self):
        self.mp = {}

    def solve(self, s1, s2):
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False

        key = (s1, s2)
        if key in self.mp:
            return self.mp[key]

        result = False
        n = len(s1)
        for i in range(1, n):
            # Check for swapped condition
            swapped = self.solve(s1[:i], s2[-i:]) and self.solve(s1[i:], s2[:-i])
            if swapped:
                result = True
                break

            # Check for not swapped condition
            not_swapped = self.solve(s1[:i], s2[:i]) and self.solve(s1[i:], s2[i:])
            if not_swapped:
                result = True
                break

        self.mp[key] = result
        return result

    def isScramble(self, s1: str, s2: str) -> bool:
        self.mp.clear()
        return self.solve(s1, s2)
