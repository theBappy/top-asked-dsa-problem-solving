# Google, Microsoft


# Right most bit = a & 1 [a=1001 & 00001]
# Right shift = a >>= 1 [eg: a = 1001 => 0100 (by right shifting of 1 digits)] [number of digits needs to shift right]
# Tc = O(log(max(a,b,c)))
# Sc = O(1)

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0
        
        while a > 0 or b > 0 or c > 0:
            if (c & 1) == 1:
                if (a & 1) == 0 and (b & 1) == 0:
                    result += 1
            else:
                result += (a & 1) + (b & 1)
            
            a >>= 1
            b >>= 1
            c >>= 1
            
        return result


# in xor, two bit same ans 0
# 0 xor 0 = 0
# 0 xor 1 = 1
# 1 xor 0 = 1
# 1 xor 1 = 0
# count number of 1 bit ?? is it right ??
# has exception

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = (a | b) ^ c
        result1 = (a & b)
        result2 = (result & result1)
        return bin(result).count('1') + bin(result2).count('1')


