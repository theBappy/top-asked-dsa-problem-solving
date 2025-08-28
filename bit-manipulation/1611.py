# Linkedin
# Min one bit operations to make integers zero

# Tc = O(1)
# Sc = O(1)

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0  # no operations
        
        F = [0] * 31
        F[0] = 1  # 1 step
        
        for i in range(1, 31):
            F[i] = 2 * F[i - 1] + 1
        
        result = 0
        sign = 1
        
        for i in range(30, -1, -1):  # left to right solve
            ith_bit = (1 << i) & n
            if ith_bit == 0:
                continue
            if sign > 0:
                result += F[i]
            else:
                result -= F[i]
            sign *= -1
        
        return result