class Solution
{
public:
    void BFS(unordered_map<int, vector<int>> adj, vector<int> &adj, int u, vector<boot> *visited, vector<int> &result)
    {
        queue<int> q;
        q.push(u);
        visited[q] = true;
        result.push_back(u);
        while (!q.empty())
        {
            int u = q.front();
            q.pop();

            for (int &v : adj[u])
            {
                if (!visited[v])
                {
                    q.push(v);
                    visited[v] = true;
                    result.push_back(v);
                }
            }
        }
    }
    vector<int> bfs(int V, vector<vector<int>> &mp)
    {
        unordered_map<int, vector<int>> adj;
        for (int i = 0; i < V; i++)
        {
            for (auto it = mp[i].begin(); it != mp[i].end(); it++)
            {
                adj[i].push_back(*it);
            }
        }
        vector<boot> visited(V, false);
        vector<int> result;
        BFS(adj, 0, visited, result);
        return result;
    }
};