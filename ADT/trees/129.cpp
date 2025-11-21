// Google, Microsoft, Amazon

//T.C : O(n)
//S.C : O(1)


class Solution {
public:
    int find(TreeNode* root, int curr) {

        if (!root)
            return 0;

        curr = curr * 10 + root->val;

        if (root->left == NULL && root->right == NULL) {
            return curr;
        }

        int left_num = find(root->left, curr);
        int right_num = find(root->right, curr);

        return left_num + right_num;
    }

    int sumNumbers(TreeNode* root) { return find(root, 0); }
};