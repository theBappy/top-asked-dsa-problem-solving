from collections import deque, defaultdict

class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        distance = [math.inf] * n
        adj = defaultdict(list)
        for u, v, cost in flights:
            adj[u].append((v, cost))
        que = deque([(src, 0)])
        distance[src] = 0
        level = 0
        while que and level <= k:
            N = len(que)
            for _ in range(N):
                u, d = que.popleft()
                for v, cost in adj[u]:
                    if distance[v] > d + cost:
                        distance[v] = d + cost
                        que.append((v, d + cost))
            level += 1
        return -1 if distance[dst] == math.inf else distance[dst]
