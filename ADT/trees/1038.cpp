// Tc = O(n)
// Sc = O(1) [system recursion stack O(height)]


class Solution {
public:
    void solve(TreeNode* root, int& sum) {
        if (!root) {
            return;
        }
        solve(root->right, sum);
        sum += root->val;
        root->val = sum;
        solve(root->left, sum);
    }
    TreeNode* bstToGst(TreeNode* root) {
        int sum = 0;
        solve(root, sum);
        return root;
    }
};