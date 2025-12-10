class Solution {
    constructor() {
        this.parent = [];
        this.rank = [];
    }

    find(x) {
        if (this.parent[x] === x)
            return x;

        this.parent[x] = this.find(this.parent[x]);
        return this.parent[x];
    }

    Union(x, y) {
        const x_parent = this.find(x);
        const y_parent = this.find(y);

        if (this.rank[x_parent] > this.rank[y_parent]) {
            this.parent[y_parent] = x_parent;
        } else if (this.rank[x_parent] < this.rank[y_parent]) {
            this.parent[x_parent] = y_parent;
        } else {
            this.parent[x_parent] = y_parent;
            this.rank[y_parent]++;
        }
    }

    // Function to detect cycle using DSU in an undirected graph.
    detectCycle(V, adj) {
        this.parent = new Array(V);
        this.rank = new Array(V).fill(0);

        for (let i = 0; i < V; i++)
            this.parent[i] = i;

        for (let u = 0; u < V; u++) {
            for (const v of adj[u]) {
                if (u < v) {
                    if (this.find(u) === this.find(v))
                        return true;
                    else {
                        this.Union(u, v);
                    }
                }
            }
        }
        return false;
    }
}