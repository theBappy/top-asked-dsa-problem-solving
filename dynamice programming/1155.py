# Amazon, Microsoft
# Tc = O(n* target * k)
# Sc = O(n * target)

# Recur + Memo
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        M = 10**9 + 7
        # Initialize the memoization table with -1
        t = [[-1] * (target + 1) for _ in range(n + 1)]
        
        def solve(n, k, target):
            if target < 0:
                return 0
            if n == 0:
                return 1 if target == 0 else 0
            if t[n][target] != -1:
                return t[n][target]
            
            ways = 0
            for face in range(1, k + 1):
                ways = (ways + solve(n - 1, k, target - face)) % M
            
            t[n][target] = ways
            return ways
        
        return solve(n, k, target)

# Example usage:
# solution = Solution()
# print(solution.numRollsToTarget(2, 6, 7))  # Example call


# Bottom Up
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        M = 10**9 + 7
        t = [[0] * (target + 1) for _ in range(n + 1)]
        t[0][0] = 1

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                ways = 0
                for face in range(1, k + 1):
                    if face <= j:
                        ways = (ways + t[i - 1][j - face]) % M

                t[i][j] = ways
        return t[n][target]

