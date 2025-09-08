

# Tc = O(n.logn)
# Sc = O(1)

class Solution(object):
    def check(self, num):
        while(num):
            if num % 10 == 0:
                return False
            num //= 10
        return True
    def getNoZeroIntegers(self, n):
        for a in range(1,n):
            b = n - a
            if self.check(a) and self.check(b):
                return [a,b]
        return []

# Tc = O(logn)
# Sc = O(1)
class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        a = n
        b = 0
        place_value = 1
        while n > 1:
            take = 1
            if n % 10 == 1:
                take = 2
            a -= take * place_value
            b += take * place_value
            n = (n - take) // 10  
            place_value *= 10
        return [a, b]