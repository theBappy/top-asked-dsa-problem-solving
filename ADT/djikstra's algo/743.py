import heapq
from collections import defaultdict
from math import inf


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        pq = []
        result = [inf] * (n + 1)
        result[k] = 0
        heapq.heappush(pq, (0, k))

        while pq:
            d, node = heapq.heappop(pq)
            for adjNode, dist in adj[node]:
                if d + dist < result[adjNode]:
                    result[adjNode] = d + dist
                    heapq.heappush(pq, (d + dist, adjNode))

        ans = max(result[1:])
        return -1 if ans == inf else ans
