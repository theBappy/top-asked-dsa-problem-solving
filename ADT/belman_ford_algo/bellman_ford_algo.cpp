
// Microsoft, Amazon, Google
// Tc = O(V*E) [but dijikstra O(E.logV), that's better]
// Sc = O(V)


class Solution {
  public:
    vector<int> bellman_ford(int V, vector<vector<int>>& edges, int src) {
        vector<int> dist(V, 1e8);
        dist[src] = 0;
        
        for(int c = 1; c<=V-1; c++) { //O(V)
            
            for(auto &edge : edges) { //O(E)
                
                int u = edge[0];
                int v = edge[1];
                int w = edge[2];
                
                if(dist[u] != 1e8 && dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                }
                
            }
            
        }
        
        //Now detect negative cycle
        for(auto &edge : edges) {
            
            int u = edge[0];
                int v = edge[1];
                int w = edge[2];
                
                if(dist[u] != 1e8 && dist[u] + w < dist[v]) {
                    return {-1};
                }
        }
        
        return dist;
    }
};
