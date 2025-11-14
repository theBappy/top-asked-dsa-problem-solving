

// Inorder traversal(right -> root -> left)
// T.C : O(n)
// S.C : O(1) (Ignoring recursion stack space)


class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        if (root == NULL)
            return 0;
        if (root->val >= low && root->val <= high) {
            return root->val + rangeSumBST(root->left, low, high) +
                   rangeSumBST(root->right, low, high);
        }
        if (root->val < low) {
            return rangeSumBST(root->right, low, high);
        }
        return rangeSumBST(root->left, low, high);
    }
};