# Google, Ola, Amazon, Microsoft

# find k'th bit??
# num & 1 << k == 0; k'th bit 0
# num & 1 << k == 1; k'th bit 1

# make k'th bit 1??
# if needs to make a set bit(eg. k = 3)
# num | 1 << 3

# Tc = O(32 * n) => O(n)
# Sc = O(1)

class Solution:
    def singleNumber(self, nums):
        result = 0
        
        for i in range(32):
            temp = 1 << i
            
            countOne = 0
            countZero = 0
            
            for num in nums:
                if (num & temp) == 0:
                    countZero += 1
                else:
                    countOne += 1
            
            if countOne % 3 == 1:
                result |= temp
        
        # Handle negative numbers
        if result >= 2**31:
            result -= 2**32
        
        return result



