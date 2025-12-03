# Samsung
# Time  - O(m*n)
# Space - O(m+n)
from collections import deque


class Solution:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def nearestExit(self, maze, entrance):
        m, n = len(maze), len(maze[0])
        que = deque([(entrance[0], entrance[1])])
        maze[entrance[0]][entrance[1]] = "+"  
        steps = 0

        while que:
            size = len(que)

            for _ in range(size):
                temp = que.popleft()

                if temp != (entrance[0], entrance[1]) and (
                    temp[0] == 0 or temp[0] == m - 1 or temp[1] == 0 or temp[1] == n - 1
                ):
                    return steps

                for dir in self.directions:
                    i, j = temp[0] + dir[0], temp[1] + dir[1]

                    if 0 <= i < m and 0 <= j < n and maze[i][j] != "+":
                        que.append((i, j))
                        maze[i][j] = "+" 

            steps += 1

        return -1
