//DSU - Union Find with Path compression
//T.C : O(n * alpha(n))
//S.C : O(n)

//DSU - Union Find with Path compression
//T.C : O(n * alpha(n)) <- alpha(n) : Inverse ackerman function, very slow for possible <= 4 operations
//S.C : O(n)

class Solution {
public:
    vector<int> parent;
    vector<int> rankArr;

    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }

    void Union(int x, int y) {
        int px = find(x);
        int py = find(y);

        if (px == py) return;

        if (rankArr[px] > rankArr[py]) {
            parent[py] = px;
        } else if (rankArr[py] > rankArr[px]) {
            parent[px] = py;
        } else {
            parent[py] = px;
            rankArr[px]++;
        }
    }

    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();

        parent.resize(n + 1);
        rankArr.resize(n + 1);

        for (int i = 1; i <= n; i++) {
            parent[i] = i;
            rankArr[i] = 0;
        }

        for (auto &edge : edges) {
            int u = edge[0];
            int v = edge[1];

            if (find(u) == find(v)) {
                return edge;  // This edge creates a cycle
            }

            Union(u, v);
        }

        return {};
    }
};
