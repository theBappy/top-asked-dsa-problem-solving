class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count = []
        for s in strs:
            countZeros = s.count("0")
            countOnes = s.count("1")
            count.append((countZeros, countOnes))
        
        # Initialize 3D memoization table: t[m][n][index]
        self.t = [[[ -1 for _ in range(len(count) + 1)] for _ in range(n + 1)] for _ in range(m + 1)]
        
        return self.solve(count, m, n, 0)
    
    def solve(self, count: List[Tuple[int, int]], m: int, n: int, index: int) -> int:
        if index >= len(count) or (m == 0 and n == 0):
            return 0
        if self.t[m][n][index] != -1:
            return self.t[m][n][index]
        
        include = 0
        if count[index][0] <= m and count[index][1] <= n:
            include = 1 + self.solve(
                count, m - count[index][0], n - count[index][1], index + 1
            )
        exclude = self.solve(count, m, n, index + 1)
        
        self.t[m][n][index] = max(include, exclude)
        return self.t[m][n][index]
