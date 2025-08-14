# Google, Facebook, Amazon, Microsoft, Goldman Sachs, Walmart
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# 8 => 2 * 2 * 2 , 6 => 2 * 3, 10 => 2 * 5
#  14 => 2 * 7 [is not an ugly number]
# 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
# 18 => 18 / 2 = 9
# 9 / 3 = 3
# 3 / 3 = 1
# 1 so [18 is a ugly number]
# 7 => 7/2 x, 7.3 x, 7/5 x, [last result != 1, so it's not an ugly number]
# Tc = n * log-base2(n) [brute force -> worst case]
# Optimal Approach, Tc = O(n) [dp => 2^a, 3^b, 5^c]
# Sc = O(n) [for n+1 array storing]

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr = [0] * (n + 1)
        # first ugly number is 1
        arr[1] = 1
        i2 = i3 = i5 = 1
        
        for i in range(2, n + 1):
            i2UglyNum = arr[i2] * 2
            i3UglyNum = arr[i3] * 3
            i5UglyNum = arr[i5] * 5
            
            minUglyNum = min(i2UglyNum, i3UglyNum, i5UglyNum)
            arr[i] = minUglyNum
            
            # Increment the pointer for the minimum ugly number
            if minUglyNum == i2UglyNum:
                i2 += 1
            if minUglyNum == i3UglyNum:
                i3 += 1
            if minUglyNum == i5UglyNum:
                i5 += 1
        
        return arr[n]  # nth ugly number
