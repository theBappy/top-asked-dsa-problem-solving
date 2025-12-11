class Solution {
public:
    vector<int> parent;
    vector<int> rank;

    int find(int x) {
        if (x == parent[x])
            return x;
        return parent[x] = find(parent[x]);
    }

    void Union(int x, int y) {
        int px = find(x);
        int py = find(y);
        if (px == py)
            return;
        if (rank[px] > rank[py]) {
            parent[py] = px;
        } else if (rank[px] < rank[py]) {
            parent[px] = py;
        } else {
            parent[px] = py;
            rank[py]++;
        }
    }

    long long countPairs(int n, vector<vector<int>>& edges) {
        parent.resize(n);
        rank.resize(n, 0);

        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        for (auto& vec : edges) {
            int u = vec[0];
            int v = vec[1];
            Union(u, v);
        }

        unordered_map<int, int> mp;
        for(int i = 0; i < n;i++){
            int head = find(i);
            mp[head]++;
        }
        long long result = 0;
        long long remainingNodes = n;

        for (auto & it : mp) {
            long long size = it.second;
            result += (size) * (remainingNodes - size);
            remainingNodes -= size;
        }
        return result;
    }
};