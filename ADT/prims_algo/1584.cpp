
// Meta, Google

// MST
// Prim's Algo(Using adj list)

class Solution {
public:
    typedef pair<int, int> P;
    int primsAlgo(vector<vector<P>>& adj, int V) {
        priority_queue<P, vector<P>, greater<P>> pq;

        pq.push({0, 0});

        vector<bool> inMST(V, false);

        int sum = 0;
        while (!pq.empty()) {
            auto p = pq.top();
            pq.pop();

            int wt = p.first;
            int node = p.second;

            if (inMST[node] == true)
                continue;

            inMST[node] = true;
            sum += wt;

            for (auto& temp : adj[node]) {
                int neighbor = temp.first;
                int neighbor_wt = temp.second;

                if (inMST[neighbor] == false) {
                    pq.push({neighbor_wt, neighbor});
                }
            }
        }
        return sum;
    }
    int minCostConnectPoints(vector<vector<int>>& points) {
        int V = points.size();

        vector<vector<P>> adj(V);

        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                int x1 = points[i][0];
                int y1 = points[i][1];
                int x2 = points[j][0];
                int y2 = points[j][1];
                int d = abs(x1 - x2) + abs(y1 - y2);
                adj[i].push_back({j, d});
                adj[j].push_back({i, d});
            }
        }
        return primsAlgo(adj, V);
    }
};

// Prim's algo (using 2d grid)