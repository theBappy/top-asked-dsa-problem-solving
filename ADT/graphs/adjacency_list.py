# adjacency matrix
def createGraph(V, edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]

    for it in edges:
        u = it[0]
        v = it[1]
        mat[u][v] = 1

        mat[v][u] = 1 #undirected graph
    return mat

def createGraph(V , edges):
    mat = [[0 for _ in range(V)] for _ in range(V)]

    for it in edges:
        u = it[0]
        v = it[1]
        mat[u][v] = 1
    return mat
# Adj list
def createGraph(V, edges):
    adj = [[] for _ in range(V)]
    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)
    return adj

def createGraph(V, edges):
    adj = [[] for _ in range(V)]
    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)
    return adj


def createGraph(V,edges):
    adj = [[] for _ in range(V)]
    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)
    return adj