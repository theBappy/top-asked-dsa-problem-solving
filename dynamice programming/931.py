# Google, Amazon, Samsung, Microsoft, OYO, makeMyTrip, OYO, Goldman Sachs
# Minimum Falling Path Sum
# Tc = O(n^2)
# Sc = O(1) [in-place]
# Bottom-Up DP
# Bottom-UP DP
class Solution:
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        for row in range(n - 2, -1, -1):
            for col in range(n):
                best = matrix[row + 1][col]
                if col > 0:
                    best = min(best, matrix[row + 1][col - 1])
                if col + 1 < n:
                    best = min(best, matrix[row + 1][col + 1])
                matrix[row][col] += best
        return min(matrix[0])