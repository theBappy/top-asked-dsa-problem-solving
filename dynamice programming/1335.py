# Recursion + Memoization(Top-down)
# Tc = O(n^2.*d)
# Sc = O(n.d)

class Solution:
    def __init__(self):
        # Initialize a memoization table with -1
        self.t = [[-1] * 11 for _ in range(301)]

    def solve(self, jd, n, idx, d):
        # Base case: If there is only one day left, do all remaining jobs in that one day
        if d == 1:
            return max(jd[idx:])  # Return the maximum difficulty of the remaining jobs
        
        # If the result is already computed, return it
        if self.t[idx][d] != -1:
            return self.t[idx][d]

        maxD = jd[idx]  # Initialize max difficulty for the current day
        finalResult = float('inf')  # Start with infinity for comparison

        # Try all possibilities of assigning jobs to the current day
        for i in range(idx, n - d + 1):
            maxD = max(maxD, jd[i])  # Update the maximum difficulty for the current day
            # Calculate the result for the remaining days and jobs
            result = maxD + self.solve(jd, n, i + 1, d - 1)
            finalResult = min(finalResult, result)  # Find the minimum result

        # Store the result in the memoization table
        self.t[idx][d] = finalResult
        return finalResult

    def minDifficulty(self, jd, d):
        n = len(jd)  # Number of jobs
        if n < d:
            return -1  # Not enough jobs to schedule
        return self.solve(jd, n, 0, d)  # Start solving from the first job and all days
