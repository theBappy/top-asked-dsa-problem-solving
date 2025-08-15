# Facebook, Amazon, Google, Microsoft
# 1, 4, 9, 16, 25,...perfect square
# Try for all possible i*i <= n
# Tc = O(n*\sqrt{n}) [the number of unique states(sub-problems->O(n), for each state recursive call we perform sqrt(n)]
# the number of perfect squares less than or equal to n is approximately O(sqrt(n))
# Memoization arr stores0 to n in O(1)
# Sc = O(n)
class Solution:
    def __init__(self):
        self.arr = [-1] * 10001  # Initialize memoization array

    def helper(self, n):
        if n == 0:
            return 0
        if self.arr[n] != -1:
            return self.arr[n]
        
        min_count = float('inf')
        i = 1
        while i * i <= n:
            result = 1 + self.helper(n - i * i)
            min_count = min(min_count, result)
            i += 1
        
        self.arr[n] = min_count
        return min_count

    def numSquares(self, n):
        return self.helper(n)
