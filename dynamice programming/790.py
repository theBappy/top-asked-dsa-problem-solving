# Google
# Tc = O(n)
# Sc = O(n)

class Solution:
    def __init__(self):
        self.M = 10**9 + 7
        self.t = [-1] * 1001  # Initialize memoization array

    def solve(self, n):
        if n == 1 or n == 2:
            return n
        if self.t[n] != -1:
            return self.t[n]
        if n == 3:
            return 5
        self.t[n] = (2 * self.solve(n - 1) % self.M + self.solve(n - 3) % self.M) % self.M
        return self.t[n]

    def numTilings(self, n):
        return self.solve(n)

# Example usage:
solution = Solution()
print(solution.numTilings(5))  # Example call
