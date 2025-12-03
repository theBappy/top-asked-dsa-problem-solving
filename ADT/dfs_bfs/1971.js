
// Using DFS
var validPath = function (n, edges, s, d) {
    const check = (mp, node, d, visited) => {
        if (node === d) return true;
        if (visited[node]) return false;
        
        visited[node] = true;
        
        for (const it of mp.get(node) || []) {
            if (check(mp, it, d, visited)) return true;
        }
        return false;
    };

    if (s === d) return true;

    const mp = new Map();

    for (const [u, v] of edges) {
        if (!mp.has(u)) mp.set(u, []);
        if (!mp.has(v)) mp.set(v, []);
        mp.get(u).push(v);
        mp.get(v).push(u);
    }

    const visited = new Array(n).fill(false);
    return check(mp, s, d, visited);
};




//Using BFS

var validPath = function (n, edges, source, destination) {
    if (source === destination) {
        return true
    }
    const adjList = new Map()
    for (const edge of edges) {
        const u = edge[0]
        const v = edge[1]
        if (!adjList.has(u)) adjList.set(u, [])
        if (!adjList.has(v)) adjList.set(v, [])
        adjList.get(u).push(v)
        adjList.get(v).push(u)
    }
    const visited = new Array(n).fill(false)
    const que = []
    que.push(source)
    visited[source] = true
    while (que.length > 0) {
        const currentNode = que.shift()
        if (currentNode === destination) {
            return true
        }
        const neighbors = adjList.get(currentNode)
        for (const neighbor of neighbors) {
            if (!visited[neighbor]) {
                visited[neighbor] = true
                que.push(neighbor)
            }
        }
    }
    return false
};