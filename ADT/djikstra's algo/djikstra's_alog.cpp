
// Tc = O((V + E) log V) (vertices + edges * logV for push and pop from pq)
// Sc = O(V+E) (distance array + pq)
class Solution {
public:
    vector<int> dijkstra(int V, vector<vector<int>> &edges, int src) {
        // Build adjacency list
        vector<vector<pair<int,int>>> adj(V);
        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].push_back({v, w});
            // adj[v].push_back({u, w}); // uncomment if graph is undirected
        }

        // Min-heap (distance, node)
        priority_queue<pair<int,int>,
                       vector<pair<int,int>>,
                       greater<pair<int,int>>> pq;

        vector<int> result(V, INT_MAX);
        result[src] = 0;
        pq.push({0, src});

        while (!pq.empty()) {
            auto [d, node] = pq.top();
            pq.pop();

            if (d > result[node]) continue;

            for (auto &p : adj[node]) {
                int adjNode = p.first;
                int wt = p.second;

                if (d + wt < result[adjNode]) {
                    result[adjNode] = d + wt;
                    pq.push({result[adjNode], adjNode});
                }
            }
        }

        return result;
    }
};


// by ordered set(ascending order store element)

/* 
📌 Why use set instead of priority_queue?
✅ Pros

We can erase outdated entries (priority_queue cannot do erase).

Cleaner logic (only one entry per node remains).

No need to check for outdated distances frequently.

❌ Cons

Slower constant factors than priority queue.

set operations are heavier (tree rotations & pointer chasing).
*/

class Solution {
public:
    vector<int> dijkstra(int V, vector<vector<int>> &edges, int src) {

        // Build adjacency list
        vector<vector<pair<int,int>>> adj(V);
        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].push_back({v, w});
            // adj[v].push_back({u, w}); // Uncomment for undirected graph
        }

        // Set stores pairs {distance, node}
        // Automatically sorted by distance
        set<pair<int,int>> st;

        vector<int> dist(V, INT_MAX);
        dist[src] = 0;

        // Insert source node with distance 0
        st.insert({0, src});

        while (!st.empty()) {
            // Get the node with the smallest distance
            auto it = st.begin(); 
            int d = it->first;
            int node = it->second;

            st.erase(it);  // remove this entry

            // Traverse neighbors
            for (auto &p : adj[node]) {
                int adjNode = p.first;
                int wt = p.second;

                // Relaxation step
                if (d + wt < dist[adjNode]) {

                    // If the adj node already has an entry in set, remove it
                    if (dist[adjNode] != INT_MAX) {
                        st.erase({dist[adjNode], adjNode});
                    }

                    // Update the distance
                    dist[adjNode] = d + wt;

                    // Insert updated pair
                    st.insert({dist[adjNode], adjNode});
                }
            }
        }

        return dist;
    }
};
