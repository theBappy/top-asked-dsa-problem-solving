#include <vector>
#include <queue>
#include <limits.h>


// using priority queue
using namespace std;

class Solution {
public:
    vector<int> dijkstra(int V, vector<vector<int>> &edges, int src) {
        // Create an adjacency list
        vector<vector<pair<int, int>>> adj(V);
        for (const auto &edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int weight = edge[2];
            adj[u].push_back({v, weight});
            adj[v].push_back({u, weight}); // If the graph is undirected
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        vector<int> result(V, INT_MAX);
        result[src] = 0; // Use src instead of source
        pq.push({0, src});

        while (!pq.empty()) {
            int d = pq.top().first;
            int node = pq.top().second;
            pq.pop();

            // If the distance is greater than the recorded distance, skip
            if (d > result[node]) continue;

            for (const auto &vec : adj[node]) {
                int adjNode = vec.first;
                int wt = vec.second;
                if (d + wt < result[adjNode]) { // Update the correct node
                    result[adjNode] = d + wt;
                    pq.push({result[adjNode], adjNode});
                }
            }
        }
        return result;
    }
};



// using ordered_set
class Solution {
  public:
    vector<int> dijkstra(int V, vector<vector<int>> &edges, int src) {
        // Create an adjacency list
        vector<vector<pair<int, int>>> adj(V);
        for (const auto &edge : edges) {
            adj[edge[0]].push_back({edge[1], edge[2]}); 
            adj[edge[1]].push_back({edge[0], edge[2]}); 
        }

        set<pair<int, int>> st;
        vector<int> result(V, INT_MAX);
        result[src] = 0; 
        st.insert({0, src});

        while (!st.empty()) {
            auto it = *st.begin();
            int d = it.first;
            int node = it.second;
            st.erase(it);

            for (const auto &vec : adj[node]) {
                int adjNode = vec.first;
                int dist = vec.second;
                if (d + dist < result[adjNode]) {

                    if (result[adjNode] != INT_MAX) {
                        st.erase({result[adjNode], adjNode});
                    }
                    result[adjNode] = d + dist;
                    st.insert({d + dist, adjNode});
                }
            }
        }
        return result;
    }
};

