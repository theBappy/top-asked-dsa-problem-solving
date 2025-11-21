// Microsoft, Amazon


class Solution {
public:
    bool check(TreeNode* l, TreeNode* r) {
        if (l == NULL && r == NULL) {
            return true;
        }
        if (l == NULL || r == NULL) {
            return false;
        }
        if (l->val == r->val && check(l->left, r->right) &&
            check(l->right, r->left)) {
            return true;
        }
        return false;
    }
    bool isSymmetric(TreeNode* root) {
        if (!root)
            return true;
        return check(root->left, root->right);
    }
};