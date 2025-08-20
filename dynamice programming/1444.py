# Google, TikTok


# Story points

# For loop for horizontal slice 
# In horizontal slice -> upper slice => apple>=1 and lower slice => apple>=k-1

# For loop for vertical slice
# In vertical slice -> left slice => apple >= 1 and right slice => apple >= k-1

# k = 1 [no need to slice] >= min need to have 1 apple in this full piece too

# Tc = O(m.n.k(m+n))
# Sc = O(m.n.k)

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        mod = 10**9 + 7
        
        # Create a 2D array to store the number of apples from (i, j) to (m-1, n-1)
        apples = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the apples array
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                apples[i][j] = apples[i + 1][j] + apples[i][j + 1] - apples[i + 1][j + 1]
                if pizza[i][j] == 'A':
                    apples[i][j] += 1
        
        # Initialize the dp array
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        
        def solve(i, j, k):
            if apples[i][j] < k:
                return 0
            if k == 1:
                return 1 if apples[i][j] >= 1 else 0
            if dp[i][j][k] != -1:
                return dp[i][j][k]
            
            ans = 0
            
            # Horizontal cuts
            for h in range(i + 1, m):
                if apples[i][j] - apples[h][j] >= 1 and apples[h][j] >= k - 1:
                    ans = (ans + solve(h, j, k - 1)) % mod
            
            # Vertical cuts
            for v in range(j + 1, n):
                if apples[i][j] - apples[i][v] >= 1 and apples[i][v] >= k - 1:
                    ans = (ans + solve(i, v, k - 1)) % mod
            
            dp[i][j][k] = ans
            return ans
        
        return solve(0, 0, k)
