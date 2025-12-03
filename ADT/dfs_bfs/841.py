class Solution:
    def dfs(self, rooms: List[List[int]], source: int, visited: List[bool]) -> None:
        visited[source] = True
        for node in rooms[source]:
            if not visited[node]:
                self.dfs(rooms, node, visited)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        self.dfs(rooms, 0, visited)
        return all(visited)