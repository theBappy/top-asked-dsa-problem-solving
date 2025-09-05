# Meta

# Tc = O(n)
# Sc = O(1)

class Solution:
    def countOrders(self, n: int) -> int:
        mod = int(1e9 + 7)
        if n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            spaces = (i - 1) * 2 + 1
            possibility = spaces * (spaces + 1) // 2
            result = (result * possibility) % mod
        return result