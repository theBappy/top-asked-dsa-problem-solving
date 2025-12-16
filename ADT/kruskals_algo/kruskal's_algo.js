class Solution {
    constructor() {
        // parent[i] stores the parent of node i
        this.parent = [];

        // rank[i] helps keep the tree shallow
        this.rank = [];
    }

    find(x) {
        /**
         * Finds the root of x
         * Uses path compression
         */
        if (this.parent[x] === x) {
            return x;
        }

        // Compress path
        this.parent[x] = this.find(this.parent[x]);
        return this.parent[x];
    }

    union(x, y) {
        /**
         * Unites the sets of x and y using rank
         */
        let xParent = this.find(x);
        let yParent = this.find(y);

        // Already in same set
        if (xParent === yParent) return;

        // Union by rank
        if (this.rank[xParent] > this.rank[yParent]) {
            this.parent[yParent] = xParent;
        } else if (this.rank[xParent] < this.rank[yParent]) {
            this.parent[xParent] = yParent;
        } else {
            this.parent[xParent] = yParent;
            this.rank[yParent]++;
        }
    }

    kruskal(edges) {
        /**
         * Runs Kruskal algorithm on sorted edges
         */
        let mstWeight = 0;

        for (let [u, v, wt] of edges) {
            // Check if adding edge creates a cycle
            if (this.find(u) !== this.find(v)) {
                this.union(u, v);
                mstWeight += wt;
            }
        }

        return mstWeight;
    }

    spanningTree(V, adj) {
        /**
         * Main MST function
         */

        // Initialize DSU arrays
        this.parent = new Array(V);
        this.rank = new Array(V).fill(0);

        for (let i = 0; i < V; i++) {
            this.parent[i] = i;
        }

        let edges = [];

        // Convert adjacency list to edge list
        for (let u = 0; u < V; u++) {
            for (let [v, wt] of adj[u]) {
                // Avoid duplicate edges
                if (u < v) {
                    edges.push([u, v, wt]);
                }
            }
        }

        // Sort edges by weight
        edges.sort((a, b) => a[2] - b[2]);

        // Apply Kruskal
        return this.kruskal(edges);
    }
}
