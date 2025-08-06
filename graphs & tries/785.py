# Microsoft, Meta, Samsung
# Is Graph Bipartite??????
'''
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.
'''
# 2 different colors paint each node, such that 2 adjacent node color will not same -> Bipartite
# Odd length cycle => Never can be Bipartite
# Even length cycle => Always be Bipartite
# Each graph can be bipartite except the graph which contains the Odd length cycle
# Dividing or Grouping graph into parts contains different properties => indicates Bipartite
# colorV = 1 - color[currColor] => x = 1 - 0 => 1 or x = 1 - 1 => 0
# Tc = O(V+E)
# Sc = O(V) [color sized array in recursion stack]

from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # -1 = uncolored, 0 = color A, 1 = color B
        
        for node in range(n):
            if color[node] == -1:  # If the node is not colored
                stack = [(node, 1)]  # Start with the current node and color 1
                while stack:
                    curr_node, curr_color = stack.pop()
                    if color[curr_node] == -1:  # If the node is uncolored
                        color[curr_node] = curr_color  # Color the node
                    else:
                        if color[curr_node] != curr_color:
                            return False  # Conflict in coloring

                    for neighbor in graph[curr_node]:
                        if color[neighbor] == -1:  # If the neighbor is uncolored
                            stack.append((neighbor, 1 - curr_color))  # Color with opposite color
                        elif color[neighbor] == curr_color:
                            return False  # Conflict in coloring

        return True

