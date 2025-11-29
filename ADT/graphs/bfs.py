from collections import deque
def bfs(adj):
    V = len(adj)
    visited = [False] * V
    res = []
    src = 0
    q = deque()
    visited[src] = True
    q.append(src)

    while q:
        curr = q.popleft()
        res.append(curr)

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

    return res