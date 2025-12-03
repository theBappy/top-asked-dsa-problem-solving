class Solution:
    def dfs(self, stones: List[List[int]], index: int, visited: List[bool]):
        visited[index] = True
        for i in range(len(stones)):
            r = stones[index][0]
            c = stones[index][1]
            if not visited[i] and (stones[i][0] == r or stones[i][1] == c):
                self.dfs(stones, i, visited)

    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        visited = [False] * n
        group = 0
        for i in range(n):
            if visited[i]:
                continue
            self.dfs(stones, i, visited)
            group += 1
        return n - group