class Solution {
public:
    typedef pair<double, int> P;
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start, int end) {
        unordered_map<int, vector<pair<int, double>>> adj;
        vector<double> result(n, 0);
        for(int i = 0; i < edges.size(); i++){
            int u = edges[i][0];
            int v = edges[i][1];
            double prob = succProb[i];
            adj[u].push_back({v, prob});
            adj[v].push_back({u, prob});
        }
        priority_queue<P> pq;

        result[start] = 1; // probability to reach start 100%
        pq.push({1.0, start});
        while(!pq.empty()){
            int currNode = pq.top().second;
            double currProb = pq.top().first;
            pq.pop();
            for(auto &temp: adj[currNode]){
                double adjProb = temp.second;
                int adjNode = temp.first;
                if(result[adjNode] < currProb*adjProb){
                    result[adjNode] = currProb*adjProb;
                    pq.push({result[adjNode], adjNode});
                }
            }
        }
        return result[end];
    }
};