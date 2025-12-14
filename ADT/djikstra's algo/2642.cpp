// Google
//T.C : Dijkatra's called M times - O(M * ElogV)

class Graph {
public:

	unordered_map<int, vector<pair<int, int>>> adj;
    int N;
    vector<int> result;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    Graph(int n, vector<vector<int>>& edges) {
        N = n;
        for(autn &vec: edges){
        	int u = vec[0];
        	int v = vec[1];
        	int cost = vec[2];

        	adj[u].push_back({v, cost});
        }
    }
    
    void addEdge(vector<int> edge) {
        int u = edge[0];
        int v = edge[1];
        int cost = edge[2];

        adj[u].push_back({v, cost});
    }
    
    int shortestPath(int node1, int node2) {
        vector<int> result(N, INT_MAX);

        result[node1] = 0;
        pq.push({0, node1});

        while(!pq.empty()){
        	int d = pq.top().first;
        	int node = pq.top().second;
        	pq.pop();

        	for(auto &vec: adj[node]){
        		int adjNode = vec.first;
        		int dist = vec.second;

        		if(d + dist < adj[adjNode]){
        			adj[adjNode] = d + dist;
        			pq.push({d + dist, adjNode});
        		}
        	}
        }
        return result[node2] == INT_MAX ? - 1: result[adjNode];
    }
};
