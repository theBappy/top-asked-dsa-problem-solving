

# Tc = O(log2(min(num1, num2)))
# Sc = O(1)

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 > 0 and num2 > 0:
            count += num1 // num2
            num1 %= num2
            num1, num2 = num2, num1
        return count

