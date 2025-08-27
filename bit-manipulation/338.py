# Amazon

# Brute force, Tc = O(n * log.n) [n for the outer loop and log.n number of bits in any number for counting the bits]
# Sc = O(n)
class Solution(object):
    def countBits(self, n):
        result =[0] * (n+1)
        for i in range(n+1):
            result[i] = bin(i).count('1')
        return result

# Optimal(Mathematical Observation)
# Tc = O(n)
# Sc = O(n)
class Solution(object):
    def countBits(self, n):
        result =[0] * (n+1)
        if n == 0:
            return result
        for i in range(1, n+1):
            if i % 2 == 1:
                result[i] = result[i//2] + 1
            else:
                result[i] = result[i//2]
        return result

