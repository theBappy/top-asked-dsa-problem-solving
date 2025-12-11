// Google
// Number of good paths

// DSU
// Tc = O(nlogn)
// Sc = O(n)


/*

📌 Explanation of Approach

A good path has:

endpoints with the same value

all nodes along path having values ≤ endpoint value

This is solved using Union-Find in increasing order of node values.

Steps

Sort nodes by values.

Activate nodes in increasing order.

Union them only with active neighbors (ensures path values are ≤ current value).

Count how many nodes of the same value fall inside each DSU component.

For each component with k such nodes, add k choose 2 good paths:

𝑘(𝑘−1) / 2


-----------
Complexity
------------

⏱️ Time Complexity Analysis
Step	Complexity
Sorting nodes by value	O(n log n)
For each edge, checking/union	O(n α(n)) ≈ O(n)
For each value, counting components	O(n log n) (due to sorting parents)
Total Time Complexity: 𝑂(𝑛log𝑛)
Space Complexity:𝑂(𝑛)

*/


var numberOfGoodPaths = function(vals, edges) {
    const n = vals.length;

    // DSU arrays
    const parent = Array.from({ length: n }, (_, i) => i);
    const rank = Array(n).fill(1);

    // Find with path compression
    const find = (x) => {
        if (parent[x] !== x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    };

    // Union by rank
    const union = (x, y) => {
        let px = find(x);
        let py = find(y);
        if (px === py) return;

        if (rank[px] > rank[py]) parent[py] = px;
        else if (rank[px] < rank[py]) parent[px] = py;
        else parent[py] = px;
    };

    // Build adjacency list
    const adj = Array.from({ length: n }, () => []);
    for (let [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    // Map value to nodes
    const valToNodes = new Map();
    for (let i = 0; i < n; i++) {
        let v = vals[i];
        if (!valToNodes.has(v)) valToNodes.set(v, []);
        valToNodes.get(v).push(i);
    }

    // Sort values
    const sortedVals = [...valToNodes.keys()].sort((a, b) => a - b);

    let result = n;   // each node is a trivial good path
    const isActive = Array(n).fill(false);

    for (let val of sortedVals) {
        const nodes = valToNodes.get(val);

        // Activate nodes and union with active neighbors
        for (let u of nodes) {
            for (let v of adj[u]) {
                if (isActive[v]) {
                    union(u, v);
                }
            }
            isActive[u] = true;
        }

        // Find parents for current value nodes
        const comp = nodes.map(u => find(u)).sort();

        // Count occurrences per parent
        let i = 0;
        while (i < comp.length) {
            let j = i, count = 0;
            while (j < comp.length && comp[j] === comp[i]) {
                j++;
                count++;
            }
            result += (count * (count - 1)) / 2;
            i = j;
        }
    }

    return result;
};
