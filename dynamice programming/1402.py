# Microsoft
# 0/1 Knapsack DP
# Max like-time co-efficient =  time * satisfaction
# Tc = O(n.logn) + O(n^2) => O(n^2)
# Sc = O(n^2)

class Solution:
    def maxSatisfaction(self, satisfaction):
        n = len(satisfaction)
        satisfaction.sort()
        dp = [[-1] * (n + 1) for _ in range(n + 1)]

        def solve(i, t):
            if i >= n:
                return 0
            if dp[i][t] != -1:
                return dp[i][t]
            include = satisfaction[i] * t + solve(i + 1, t + 1)
            exclude = solve(i + 1, t)
            dp[i][t] = max(include, exclude)
            return dp[i][t]

        return solve(0, 1)

# Example usage:
# solution = Solution()
# print(solution.maxSatisfaction([-1, -8, 0, 5, -9]))  # Example input



# Bottom up
# State definition: dp[i][j] = max value till 0...i food and time is j currently
class Solution:
    def maxSatisfaction(self, satisfaction):
        # Sort the satisfaction levels in ascending order
        satisfaction.sort()
        n = len(satisfaction)
        
        # Initialize a DP table with dimensions (n+1) x (n+1) filled with negative infinity
        dp = [[float('-inf')] * (n + 1) for _ in range(n + 1)]
        
        # At time 0, the maximum satisfaction is 0 since no cooking has started
        for i in range(n + 1):
            dp[i][0] = 0
        
        # Start filling the DP table
        for i in range(1, n + 1):
            for time in range(1, n + 1):
                # Include the current food item
                include = satisfaction[i - 1] * time + dp[i - 1][time - 1]
                # Exclude the current food item
                exclude = dp[i - 1][time]
                # Take the maximum of including or excluding the current food item
                dp[i][time] = max(include, exclude)
        
        # Find the maximum satisfaction across all times
        ans = 0
        for time in range(1, n + 1):
            ans = max(ans, dp[n][time])
        
        return ans


