
// Google

class Solution {
public:
    int minDiff = INT_MAX;
    TreeNode* prev;
    void inOrder(TreeNode* root) {
        if (!root) {
            return;
        }
        inOrder(root->left);
        if (prev != NULL) {
            minDiff = min(minDiff, root->val - prev->val);
        }
        prev = root;
        inOrder(root->right);
    }
    int getMinimumDifference(TreeNode* root) {
        prev = NULL;
        inOrder(root);
        return minDiff;
    }
};