# Google
# Tc = O(n+m)
# Sc = O(n+m)

class Solution:
    def dfs(self, rooms, source, visited):
        visited[source] = True
        for node in rooms[source]:
            if not visited[node]:
                self.dfs(rooms, node, visited)
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [False] * n
        self.dfs(rooms, 0, visited)
        for x in visited:
            if not x:
                return False
        return True
         
