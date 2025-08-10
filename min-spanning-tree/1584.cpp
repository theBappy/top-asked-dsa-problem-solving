// Manhattan Distance = [x1-x2] + [y1-y2]
// Prim's Algorithm


class Solution {
public: 

    typedef pair<int, int> P;

    int primsAlgo(vector<vector<P>>& adj, int V) {
        priority_queue<P, vector<P>, greater<P>> pq;
        pq.push({0, 0}); // Start from node 0 with weight 0
        vector<bool> inMST(V, false);
        int sum = 0;

        while (!pq.empty()) {
            auto p = pq.top();
            pq.pop();
            int wt = p.first;
            int node = p.second;

            if (inMST[node]) // If the node is already in MST, skip it
                continue;

            inMST[node] = true; // Mark the node as included in MST
            sum += wt; // Add the weight to the total sum

            for (auto &tmp : adj[node]) {
                int neighbor = tmp.first; // Get the neighbor node
                int neighbor_wt = tmp.second; // Get the weight of the edge

                if (!inMST[neighbor]) { // If the neighbor is not in MST
                    pq.push({neighbor_wt, neighbor}); // Push it to the priority queue
                }
            }
        }
        return sum; // Return the total weight of the MST
    }

    int minCostConnectPoints(vector<vector<int>>& points) {
        int V = points.size();
        vector<vector<P>> adj(V);
        
        for (int i = 0; i < V; i++) {
            for (int j = i + 1; j < V; j++) {
                int x1 = points[i][0];
                int y1 = points[i][1];
                int x2 = points[j][0];
                int y2 = points[j][1];

                int d = abs(x1 - x2) + abs(y1 - y2); // Calculate Manhattan distance

                adj[i].push_back({j, d}); // Add edge to adjacency list
                adj[j].push_back({i, d}); // Add edge to adjacency list
            }
        }
        return primsAlgo(adj, V); // Call Prim's algorithm
    }
};
