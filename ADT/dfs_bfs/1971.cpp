// Using DFS
class Solution {
public:
    bool check(unordered_map<int, vector<int>>& mp, int node, int destination,
               vector<bool>& visited) {
        if (node == destination)
            return true;
        if (visited[node])
            return false;
        visited[node] = true;
        for (auto& it : mp[node]) {
            if (check(mp, it, destination, visited))
                return true;
        }
        return false;
    }
    bool validPath(int n, vector<vector<int>>& edges, int source,
                   int destination) {
        if (source == destination)
            return true;
        unordered_map<int, vector<int>> mp;
        for (vector<int>& vec : edges) {
            int u = vec[0];
            int v = vec[1];
            mp[u].push_back(v);
            mp[v].push_back(u);
        }
        vector<bool> visited(n, false);
        return check(mp, source, destination, visited);
    }
};


// Using BFS
class Solution {
public:    
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        unordered_map<int, vector<int>> mp;
        
        for(vector<int> &vec : edges) {
            int u = vec[0];
            int v = vec[1];
            
            mp[u].push_back(v);
            mp[v].push_back(u);
        }
        
        vector<bool> visited(n, false);
        
        queue<int> que;
        que.push(source);
        visited[source] = true;
        
        while(!que.empty()) {
            int node = que.front();
            que.pop();
            if(node == destination)
                return true;

            for(auto &it : mp[node]) {
                if(!visited[it]) {
                    visited[it] = true;
                    que.push(it);
                }
            }
        }
        
        return false;
    }
};