# Google, Meta

# Tc =>
# cuts position, {c1, c2, c3, ...m} for each left and right and for left and right there is also a for loop for possibility
# {l, r} => O(m^2 * m) => O(m^3)
# Sc = O(m^2) [memoization table for each pair of cuts and recursion stack O(m) so dominating O(m^2) is the space complexity]

class Solution(object):
    def __init__(self):
        self.t = [[-1] * 103 for _ in range(103)]

    def solve(self, cuts, start, end):
        if end - start < 2:
            return 0
        if self.t[start][end] != -1:
            return self.t[start][end]  # Return memoized result
        
        result = float('inf')
        for index in range(start + 1, end):
            cost = (cuts[end] - cuts[start]) + self.solve(cuts, start, index) + self.solve(cuts, index, end)
            result = min(result, cost)
        
        self.t[start][end] = result  # Store the result in the memoization table
        return result

    def minCost(self, n, cuts):
        cuts.sort()
        cuts = [0] + cuts + [n]  # Add starting and ending points
        return self.solve(cuts, 0, len(cuts) - 1)

# Example usage:
# solution = Solution()
# print(solution.minCost(n, cuts))

