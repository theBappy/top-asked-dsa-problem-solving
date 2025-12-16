
// Tc = O(E log E)
// Sc = O(V + E)
class Solution {
public:
    vector<int> parent, rank;

    int find(int x) {
        if (x == parent[x]) return x;
        return parent[x] = find(parent[x]); // path compression
    }

    void Union(int x, int y) {
        int x_parent = find(x);
        int y_parent = find(y);

        if (x_parent == y_parent) return;

        // union by rank
        if (rank[x_parent] > rank[y_parent]) {
            parent[y_parent] = x_parent;
        } 
        else if (rank[x_parent] < rank[y_parent]) {
            parent[x_parent] = y_parent;
        } 
        else {
            parent[x_parent] = y_parent;
            rank[y_parent]++;
        }
    }

    int Kruskal(vector<vector<int>> &edges) {
        int sum = 0;

        // O(E) * 4*(alpha) => Inverse ackerman function
        for (auto &e : edges) {
            int u = e[0];
            int v = e[1];
            int wt = e[2];

            if (find(u) != find(v)) {
                Union(u, v);
                sum += wt;
            }
        }
        return sum;
    }

    int spanningTree(int V, vector<vector<int>> adj[]) {
        parent.resize(V);
        rank.resize(V, 0);

        for (int i = 0; i < V; i++) parent[i] = i;

        vector<vector<int>> edges;

    	// O(V + E)
        // build edge list (avoid duplicates)
        for (int u = 0; u < V; u++) {
            for (auto &temp : adj[u]) {
                int v = temp[0];
                int wt = temp[1];
                if (u < v) {
                    edges.push_back({u, v, wt});
                }
            }
        }

        // ElogE
        sort(edges.begin(), edges.end(),
             [](vector<int>& a, vector<int>& b) {
                 return a[2] < b[2];
             });

        return Kruskal(edges);
    }
};
