
// Using DFS
//T.C : O(m* (V+E)), we try DFS m times
//S.C : O(V+E)

class Solution {
public:
    char DFSFindMinChar(unordered_map<char, vector<char>>& adj, char curr_ch,
                        vector<int>& visited) {
        visited[curr_ch - 'a'] = 1; // mark it as visited
        char minChar = curr_ch;
        for (char& v : adj[curr_ch]) {
            if (visited[v - 'a'] == 0) {
                minChar = min(minChar, DFSFindMinChar(adj, v, visited));
            }
        }
        return minChar;
    }
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        int n = s1.length();
        int m = baseStr.length();
        unordered_map<char, vector<char>> adj;
        for (int i = 0; i < n; i++) {
            char u = s1[i];
            char v = s2[i];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        string result;
        for (int i = 0; i < m; i++) {
            char ch = baseStr[i];
            vector<int> visited(26, 0); // for this ch, none is visited as of
                                        // now
            char minChar = DFSFindMinChar(adj, ch, visited);
            result.push_back(minChar);
        }
        return result;
    }
};