# Microsoft, Linkedin

# Associative => (a^b)^c = a^(b^c)
# Commutative => (a^b) = (b^a)
# XOR => 1^1=0, 0^0=0, 1^0=1, 0^1=1, 10^10=0 [two same number xor = 0]
# Tc = O(n)
# Sc = O(1)

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        for i in range(n-1, 0, -1):
            pref[i] = pref[i] ^ pref[i-1]
        return pref