
// By Prim's Algorithm

// Tc = O(E*(logE + logE) => O(ElogE)
//“Lazy Prim’s runs in O(E log E), which simplifies to O(E log V) since E ≤ V².”

class Solution
{
    typedef pair<int, int> P; // {weight, node}
    
    public:
    int spanningTree(int V, vector<vector<int>> adj[]) {

        priority_queue<P, vector<P>, greater<P>> pq;
        pq.push({0, 0});  // {weight, starting node}

        vector<bool> inMST(V, false);
        int sum = 0;

        while (!pq.empty()) {

            auto p = pq.top();
            pq.pop();   // ✅ MUST pop

            int wt = p.first;
            int node = p.second;

            // Skip if already included
            if (inMST[node]) continue;

            // Include node in MST
            inMST[node] = true;
            sum += wt;

            // Push adjacent edges
            for (auto &temp : adj[node]) {
                int neighbor = temp[0];
                int neighbor_wt = temp[1];

                if (!inMST[neighbor]) {
                    pq.push({neighbor_wt, neighbor});
                }
            }
        }

        return sum;
    }
};

