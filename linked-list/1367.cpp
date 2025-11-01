// Recursion leap of faith
// Tc = O(n*m) [n = root length, m = linked list length] (from each root trying finding m length linked list)
// Sc = O(n+m) [if skewed tree, for recursion stack]
class Solution {
public:
    bool check(ListNode* head, TreeNode* root) {
        if (head == NULL)
            return true;
        if (root == NULL)
            return false;
        if (head->val != root->val) {
            return false;
        }
        return check(head->next, root->left)
        || check(head->next, root->right);
    }
    bool isSubPath(ListNode* head, TreeNode* root) {
        if (root == NULL)
            return false;
        return check(head, root) || isSubPath(head, root->left) ||
               isSubPath(head, root->right);
    }
};