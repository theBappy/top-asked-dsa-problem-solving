// Shortest Path in Weighted undirected graph(GFG)
// Tc = O(m.logn)
// Sc = O(n + m)

class Solution {
public:
    vector<int> shortestPath(int n, int m, vector<vector<int>>& edges) {

        vector<vector<pair<int,int>>> adj(n+1);
        for (auto &vec : edges) {
            int u = vec[0], v = vec[1], w = vec[2];
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }

        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
        vector<int> dist(n+1, INT_MAX);
        vector<int> parent(n+1);

        for (int i = 1; i <= n; i++) parent[i] = i;

        dist[1] = 0;
        pq.push({0, 1});

        while (!pq.empty()) {
            auto [d, node] = pq.top();
            pq.pop();

            // Important: skip stale distances
            if (d != dist[node]) continue;

            for (auto &it : adj[node]) {
                int adjNode = it.first;
                int weight  = it.second;

                if (d + weight < dist[adjNode]) {
                    dist[adjNode] = d + weight;
                    parent[adjNode] = node;
                    pq.push({dist[adjNode], adjNode});
                }
            }
        }

        // No path exists
        if (dist[n] == INT_MAX) return {-1};

        // Reconstruct path
        vector<int> path;
        int node = n;

        while (parent[node] != node) {
            path.push_back(node);
            node = parent[node];
        }

        path.push_back(1);
        reverse(path.begin(), path.end());
        return path;
    }
};
