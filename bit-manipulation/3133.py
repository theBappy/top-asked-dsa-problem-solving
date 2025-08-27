# Google
# Tc = O(n)
# Sc = O(1)

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        k = n - 1
        res = x
        bit = 0
        i = 0
        while k > 0:
            # check if current bit in x is 0
            if (x >> i) & 1 == 0:
                # take lowest bit of k
                if (k >> bit) & 1:
                    res |= (1 << i)
                bit += 1
            i += 1
            if (1 << bit) > k:  # small optimization
                break
        return res
