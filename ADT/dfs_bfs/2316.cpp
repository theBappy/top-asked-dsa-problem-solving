class Solution {
public:
    void dfs(int u, unordered_map<int, vector<int>>& adj, vector<bool>& visited,
             long long& sizeOfComponent) {
        visited[u] = true;
        sizeOfComponent++;
        for (int &v : adj[u]) {
            if (!visited[v]) {
                dfs(v, adj, visited, sizeOfComponent);
            }
        }
    }
    long long countPairs(int n, vector<vector<int>>& edges) {
        unordered_map<int, vector<int>> adj;
        for (auto& vec : edges) {
            int u = vec[0];
            int v = vec[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        vector<bool> visited(n, false);
        long long remainingNodes = n;
        long long result = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                long long sizeOfComponent = 0;
                dfs(i, adj, visited, sizeOfComponent);
                result +=
                    (sizeOfComponent) * (remainingNodes - sizeOfComponent);
                remainingNodes -= sizeOfComponent;
            }
        }
        return result;
    }
};