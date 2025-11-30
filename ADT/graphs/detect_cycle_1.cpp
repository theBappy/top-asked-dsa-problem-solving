// Tc = O(V + E)

// Using DFS
bool isCycleDFS(vector<int> g[], int start, vector<bool>& visited, int parent) {
    visited[start] = true;
    
    vector<int>::iterator it;
    for(it = g[start].begin(); it != g[start].end(); it++) {
        if(*it == parent)
            continue;
        if(visited[*it] == true)
            return true;
        if(isCycleUtil(g, *it, visited, start))
            return true;
            
    }
    return false;
}

bool isCyclic(vector<int> g[], int V) {
    vector<bool> visited(V, false);
    
    for(int i = 0; i<V; i++) {
        if(visited[i] == false && isCycleUtil(g, i, visited, -1))
            return true;
    }
    return false;
}


// Using BFS
class Solution {
  public:
    bool isCycleBFS(vector<int> g[], int V, int start, vector<bool>& visited) {
        queue<pair<int, int>> que;
        que.push({start, -1});
        visited[start] = true;
        while(!que.empty()) {
            int curr   = que.front().first;
            int parent = que.front().second;
            que.pop();
            
            for(auto x : g[curr]) {
                if(visited[x] == false) {
                    que.push({x, curr});
                    visited[x] = true;
                }
                else if(x != parent)
                    return true;
            }
        }
        
        return false;
    }

  
    // Function to detect cycle in an undirected graph.
    bool isCycle(int V, vector<int> adj[]) {
        
        vector<bool> visited(V, false);
        
        for(int i = 0; i<V; i++) {
            if(!visited[i] && isCycleBFS(adj, V, i, visited)) {
                return true;
            }
        }
        
        return false;
        
    }
};