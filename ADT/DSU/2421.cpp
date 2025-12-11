// Google
// Number of good paths

// DSU
// Tc = O(nlogn)
// Sc = O(n)

class Solution {
public:
    
    vector<int> parent;
    vector<int> rank;
    
    int find (int x) {
        if (x == parent[x]) 
            return x;
        
        return parent[x] = find(parent[x]);
    }
    
    void Union (int x, int y) {
        int x_parent = find(x);
        int y_parent = find(y);
        
        if (x_parent == y_parent) 
            return;
        
        if(rank[x_parent] > rank[y_parent]) {
            parent[y_parent] = x_parent;
        } else if(rank[x_parent] < rank[y_parent]) {
            parent[x_parent] = y_parent;
        } else {
            parent[x_parent] = y_parent;
        }
    }
    
    int numberOfGoodPaths(vector<int>& vals, vector<vector<int>>& edges) {
        int n = vals.size();
        
        parent.resize(n);
        rank.resize(n, 1);
        
        for(int i = 0; i<n; i++) {
            parent[i] = i;
        }
        
        unordered_map<int, vector<int>> adj;
        
        for(vector<int> &vec : edges) {
            int u = vec[0];
            int v = vec[1];
            
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        
        
        map<int, vector<int>> val_to_nodes;
        
        for (int i = 0; i < n; i++) {
            int value = vals[i];
            
            val_to_nodes[value].push_back(i);
        }
        
        int result = n;
        
        vector<bool> is_active(n, false); //non active in the beginning
        
        for (auto &it : val_to_nodes) {
            
            vector<int> nodes = it.second;
            
            for (int &u : nodes) {
                
                for (int &v: adj[u]) {
                    if (is_active[v]) {
                        Union(u, v);
                    }
                }
                is_active[u] = true;
            }
            
            vector<int> head_parent;
            
            for (int &u : nodes) 
                head_parent.push_back(find(u));
            
            sort(head_parent.begin(), head_parent.end());
                        
            int sz = head_parent.size();
            
            for (int j = 0; j < sz; j++) {
                long long count = 0;
                
                int curr_parent = head_parent[j];
                
                while (j < sz && head_parent[j] == curr_parent) {
                    j++, 
                    count++;
                }
                j--;
                
                result += (count * (count - 1))/2;
            }
        }
        
        return result;
    }
};