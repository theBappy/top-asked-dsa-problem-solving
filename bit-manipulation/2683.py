# Samsung, Apple, Microsoft, Netflix
# Tc = O(n)
# Sc = O(n)

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        original = [0] * n
        original[0] = 0
        for i in range(n-1):
            original[i+1] = original[i] ^ derived[i]
        if original[n-1] ^ original[0] == derived[n-1]:
            return True
        original[0] = 1
        for i in range(n-1):
            original[i+1] = original[i] ^ derived[i]
        if original[n-1] ^ original[0] == derived[n-1]:
            return True
        return False

# Approach-2
# Tc = O(n)
# Sc = O(1)
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        XOR = 0
        for x in derived:
            XOR = XOR ^ x
        return XOR == 0