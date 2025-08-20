//  Meta, Microsoft, Amazon
// Recur+Memo(Top-down)
class Solution {
public:
    int m, n;
    int t[501][501];
    int solve(int i, int j, vector<int>& nums1, vector<int>& nums2) {
        if (i >= m || j >= n) {
            return 0;
        }
        if (t[i][j] != -1)
            return t[i][j];
        if (nums1[i] == nums2[j]) {
            return t[i][j] = 1 + solve(i + 1, j + 1, nums1, nums2);
        } else {
            int fix_i = solve(i, j + 1, nums1, nums2);
            int fix_j = solve(i + 1, j, nums1, nums2);
            return t[i][j] = max(fix_i, fix_j);
        }
    }
    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
        m = nums1.size();
        n = nums2.size();
        memset(t, -1, sizeof(t));
        return solve(0, 0, nums1, nums2);
    }
};

// Bottom up
// State define: t[i][j] = x, maximum lines that we can draw with nums1 of length i and nums2 of length j
class Solution {
public:
    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        vector<vector<int>> t(m + 1, vector<int>(n + 1));
        for (int i = 0; i < m + 1; i++) {
            for (int j = 0; j < n + 1; j++) {
                if (i == 0 || j == 0) {
                    t[i][j] = 0;
                }else if(nums1[i-1] == nums2[j-1]){
                    t[i][j] = 1 + t[i-1][j-1];
                }else{
                    t[i][j] = max(t[i][j-1], t[i-1][j]);
                }
            }
        }
        return t[m][n];
    }
};