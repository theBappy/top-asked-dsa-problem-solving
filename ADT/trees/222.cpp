// Amazon, Meta, Amazon
// Tc = O(log(n) * log(n))


class Solution {
public:
    int leftTreeHeight(TreeNode* root) {
        if (!root)
            return 0;
        int lh = 0;
        TreeNode* temp = root;
        while (temp) {
            temp = temp->left;
            lh++;
        }
        return lh;
    }
    int rightTreeHeight(TreeNode* root) {
        if (!root)
            return 0;
        int rh = 0;
        TreeNode* temp = root;
        while (temp) {
            temp = temp->right;
            rh++;
        }
        return rh;
    }
    int countNodes(TreeNode* root) {
        if (!root)
            return 0;
        int lh = leftTreeHeight(root);
        int rh = rightTreeHeight(root);
        if (lh == rh)
            return pow(2, lh) - 1;
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};