
class Solution {
public:
    typedef long long ll;
    typedef pair<ll, ll> P;
    
    vector<int> dijkstra(unordered_map<int, vector<P>>& adj, int src, int n) {
        priority_queue<P, vector<P>, greater<P>> pq;

        vector<int> dist(n, INT_MAX);
        vector<bool> visited(n, false);

        dist[src] = 0;

        pq.push({0, src});

        while(!pq.empty()) {

            ll  currWt   = pq.top().first;
            int currNode = pq.top().second;
            pq.pop();
        
                        
            if(visited[currNode] == true) {
                continue;
            }


            for(auto adj: adj[currNode]) {
                int nextNode = adj.first;
                ll nextWt = adj.second;

                if(dist[nextNode] > currWt + nextWt) {
                    dist[nextNode] = currWt + nextWt;
                    pq.push({currWt + nextWt, nextNode});
                }
            }
            
            visited[currNode] = true;


        }

        return dist;
    }
    
    vector<bool> findAnswer(int n, vector<vector<int>>& edges) {
        int E = edges.size();
        
        unordered_map<int, vector<P>> adj;
        for(auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }
        
        vector<int> fromSrc  = dijkstra(adj, 0, n);
        vector<int> fromDest = dijkstra(adj, n-1, n);
        
        vector<bool> result(E, false);
        
        for(int i = 0; i < E; i++) {
            
            int u = edges[i][0];
            int v = edges[i][1];
            int w = edges[i][2];
            
            ll distFromSrc  = fromSrc[u]; //x
            ll distFromDest = fromDest[v]; //y
            
            if(distFromSrc + w + distFromDest == fromSrc[n-1]) {
                result[i] = true;
            }
            
            
            distFromSrc  = fromSrc[v]; //x
            distFromDest = fromDest[u]; //y
            if(distFromSrc + w + distFromDest == fromSrc[n-1]) {
                result[i] = true;
            }
            
        }
        
        return result;
    }
};



