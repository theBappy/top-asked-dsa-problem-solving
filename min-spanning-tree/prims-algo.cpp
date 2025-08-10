// Prim's Algorithm to Find the Sum of minimum spanning tree
// Tc = O(E.logV)
// Sc = O(V+E)
#include <queue>
#include <utility>

class Solution {
public:
    int spanningTree(int V, std::vector<std::vector<int>>& edges) {
        // Step 1: Build the adjacency list from the given edges.
        // It's a vector of lists, where each list stores pairs of {neighbor, weight}.
        std::vector<std::vector<std::pair<int, int>>> adj(V);
        for (const auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            adj[u].push_back({v, w});
            adj[v].push_back({u, w}); // Assuming an undirected graph
        }

        // Step 2: Initialize data structures for Prim's algorithm.
        // Priority queue to store {weight, node} pairs.
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> pq;
        pq.push({0, 0}); // Start from node 0 with a weight of 0.

        // Boolean vector to track which nodes are already in the MST.
        std::vector<bool> inMST(V, false);

        int sum = 0; // Total weight of the MST.

        // Step 3: Main loop of Prim's algorithm.
        // O(E*(LogE+logE)) => O(E.logE)
        while (!pq.empty()) {
            auto p = pq.top();
            pq.pop(); // log(E)

            int wt = p.first;
            int node = p.second;

            // If the node is already in the MST, skip it.
            if (inMST[node]) {
                continue;
            }

            // Add the node to the MST and update the total weight.
            inMST[node] = true;
            sum += wt;

            // Explore the neighbors of the current node.
            for (auto& neighbor_data : adj[node]) {
                int neighbor = neighbor_data.first;
                int neighbor_wt = neighbor_data.second;

                // If the neighbor is not yet in the MST, add it to the priority queue.
                if (!inMST[neighbor]) {
                    pq.push({neighbor_wt, neighbor}); // log(E)
                }
            }
        }
        return sum;
    }
};