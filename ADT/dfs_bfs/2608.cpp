
class Solution {
public:
    int findShortestCycle(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);
        
        // Build the undirected graph
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }
        
        int result = INT_MAX;
        
        // BFS from each node
        for (int start = 0; start < n; start++) {
            vector<int> dist(n, -1);
            vector<int> parent(n, -1);
            queue<int> q;
            
            dist[start] = 0;
            q.push(start);
            
            while (!q.empty()) {
                int u = q.front(); q.pop();
                
                for (int v : graph[u]) {
                    if (dist[v] == -1) {
                        dist[v] = dist[u] + 1;
                        parent[v] = u;
                        q.push(v);
                    } else if (parent[u] != v) {
                        // Found a cycle
                        result = min(result, dist[u] + dist[v] + 1);
                    }
                }
            }
        }
        
        return result == INT_MAX ? -1 : result;
    }
};
