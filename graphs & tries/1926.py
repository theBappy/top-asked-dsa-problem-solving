# Samsung, Netflix
# Exit the maze
# BFS(shortest path)
# Boundary(i, j); i == 0 or i == m-1 || j == 0 or j == n-1
# (i,j) != entrance
# Entrance cannot be count as exit
# Tc = O(m.n)
# Sc = O(m.n)

import collections

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m, n = len(maze), len(maze[0])
        
        # Using a deque for an efficient queue data structure
        queue = collections.deque([(entrance[0], entrance[1], 0)])
        
        # Mark the entrance as a wall to prevent going back
        maze[entrance[0]][entrance[1]] = '+'
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            i, j, steps = queue.popleft()
            
            # Check for an exit. An exit is any empty cell on the border
            # that is not the entrance itself.
            if steps > 0 and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                return steps
            
            # Explore neighbors
            for dx, dy in directions:
                new_i, new_j = i + dx, j + dy
                
                # Check if the new cell is within bounds and is an empty path
                if 0 <= new_i < m and 0 <= new_j < n and maze[new_i][new_j] == '.':
                    # Mark the new cell as visited by changing it to a wall
                    maze[new_i][new_j] = '+'
                    # Add the new cell to the queue with an incremented step count
                    queue.append((new_i, new_j, steps + 1))
        
        # If the queue becomes empty and no exit was found, return -1
        return -1        
