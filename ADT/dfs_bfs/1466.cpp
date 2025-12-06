// Meta
// Using DFS
class Solution {
public:
    int edgesToReverse = 0;

    void dfs(int curr, int parent,
             unordered_map<int, vector<pair<int, int>>>& adj) {

        for (auto &P : adj[curr]) {
            int nextNode = P.first;
            int isOutgoingFromOriginal = P.second; // 1 = originally curr -> nextNode

            if (nextNode != parent) {
                // If edge was originally directed away from 0, it must be reversed
                if (isOutgoingFromOriginal == 1) {
                    edgesToReverse++;
                }
                dfs(nextNode, curr, adj);
            }
        }
    }

    int minReorder(int n, vector<vector<int>>& connections) {
        unordered_map<int, vector<pair<int, int>>> adj;

        for (auto &vec : connections) {
            int a = vec[0];
            int b = vec[1];

            adj[a].push_back({b, 1}); // original direction a → b
            adj[b].push_back({a, 0}); // reverse direction b → a (cost 0)
        }

        dfs(0, -1, adj);

        return edgesToReverse;
    }
};
