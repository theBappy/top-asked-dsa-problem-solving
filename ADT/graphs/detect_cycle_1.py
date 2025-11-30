def is_cyclic_dfs(g, start, visited, parent):
    visited[start] = True
    for neighbor in g[start]:
        if neighbor == parent:
            continue
        if visited[neighbor]:
            return True
        if is_cyclic_dfs(g, neighbor, visited, start):
            return True
    return False
def is_cyclic(g, V):
    visited = [False] * V
    for i in range(V):
        if not visited[i] and is_cyclic_dfs(g, i, visited, -1):
            return True
    return True
        