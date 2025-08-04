class Solution {
    dfs(u, adj, visited, result) {
        visited.add(u);
        for (const [v, d] of adj.get(u)) {
            // Update the minimum score found so far
            result[0] = Math.min(result[0], d);
            if (!visited.has(v)) {
                this.dfs(v, adj, visited, result);
            }
        }
    }

    minScore(n, roads) {
        const adj = new Map();
        
        // Build the adjacency list
        for (const [u, v, d] of roads) {
            if (!adj.has(u)) adj.set(u, []);
            if (!adj.has(v)) adj.set(v, []);
            adj.get(u).push([v, d]);
            adj.get(v).push([u, d]);
        }
        
        const visited = new Set();
        const result = [Infinity]; // Initialize result with Infinity
        
        // Start DFS from node 1 (assuming nodes are 1-indexed)
        this.dfs(1, adj, visited, result);
        
        return result[0]; // Return the minimum score found
    }
}
