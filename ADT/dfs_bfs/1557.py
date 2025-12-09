# Google
from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [False] * n
        for u, v in edges:
            indegree[v] = True
        result = [i for i in range(n) if not indegree[i]]
        return result