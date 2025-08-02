
// DFS
class Solution {
    validPath(n, edges, source, destination) {
        const adj = new Map();
        for (const [u, v] of edges) {
            if (!adj.has(u)) adj.set(u, []);
            if (!adj.has(v)) adj.set(v, []);
            adj.get(u).push(v);
            adj.get(v).push(u);
        }
        const visited = new Set();
        
        const dfs = (node) => {
            if (node === destination) {
                return true;
            }
            visited.add(node);
            for (const neighbor of adj.get(node)) {
                if (!visited.has(neighbor)) {
                    if (dfs(neighbor)) {
                        return true;
                    }
                }
            }
            return false;
        };
        
        return dfs(source);
    }
}

