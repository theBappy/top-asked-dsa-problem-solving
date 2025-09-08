
# Google, Meta

#  composed of the minimum number of powers of 2 that sum to n => Binary Representation
# Tc = O(Q * 32) => O(Q) [linear, Q=query, 32 max powers array]
# Sc = O(32) => O(1) [as questioned mentioned powers array required]
class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        M = 10**9 + 7
        powers = []
        result = []

        # Build powers array
        for i in range(32):
            if (n & (1 << i)) != 0:  # ith bit is set
                powers.append(1 << i)

        for query in queries:
            start = query[0]
            end = query[1]

            product = 1
            for i in range(start, end + 1):
                product = (product * powers[i]) % M

            result.append(product)

        return result