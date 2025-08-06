// Is graph Bipartite? => DFS approach
class Solution {
public:
    bool checkBipartiteDFS(vector<int> adj[], int curr, vector<int>& color, int currColor) {
        color[curr] = currColor; // color the current node
        // now go to adjacent nodes and try to color them with a different color
        for (int &v : adj[curr]) {
            if (color[v] == color[curr]) {
                return false; // same color as current node
            }
            if (color[v] == -1) { // never colored or visited
                int colorOfV = 1 - currColor; // alternate color
                if (!checkBipartiteDFS(adj, v, color, colorOfV)) {
                    return false; // if any adjacent node fails, return false
                }
            }
        }
        return true; // all adjacent nodes can be colored properly
    }

    bool isBipartite(int V, vector<int> adj[]) {
        vector<int> color(V, -1); // no node colored at the start
        // red = 1, green = 0
        for (int i = 0; i < V; i++) {
            if (color[i] == -1) { // if the node is not colored
                if (!checkBipartiteDFS(adj, i, color, 1)) {
                    return false; // if any component is not bipartite
                }
            }
        }
        return true; // all components are bipartite
    }
};
