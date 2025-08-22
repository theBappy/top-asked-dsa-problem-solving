class Solution {
public:
    int t[103][103];
    int solve(vector<int>& cuts, int left, int right) {
        if (right - left < 2) {
            return 0;
        }
        if(t[left][right] != -1)
            return t[left][right];
        int result = INT_MAX;
        for (int index = left + 1; index <= right - 1; index++) {
            int cost = (cuts[right] - cuts[left]) + solve(cuts, left, index) + solve(cuts, index, right);
            result = min(result, cost);
        }
        t[left][right] = result;
        return t[left][right];
    }
    int minCost(int n, vector<int>& cuts) {
        sort(begin(cuts), end(cuts));
        cuts.insert(begin(cuts), 0); // starting point of stick
        cuts.push_back(n);           // ending point of stick
        // length of stick => cuts[r] - cuts[l] = n - 0
        memset(t, -1, sizeof(t));
        return solve(cuts, 0, cuts.size() - 1);
    }
};