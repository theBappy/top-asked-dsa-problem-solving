# GOOGLE
# Stones Removed
# Tc = O(n^2)
# Sc = O(n^2)
class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        n = len(stones)
        visited = [False] * n
        groups = n
        def dfs(index):
            visited[index] = True
            r, c = stones[index]
            for i in range(n):
                if not visited and (stones[i][0] == r or stones[i][1] == c):
                    dfs(i)
        for i in range(n):
            if not visited[i]:
                dfs(i)
                groups += 1
        return n - groups