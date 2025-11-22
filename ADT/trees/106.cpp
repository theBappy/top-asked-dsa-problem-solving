// Google


class Solution {
public:
    TreeNode* solve(vector<int>& inorder, vector<int>& postorder, int inStart,
                    int inEnd, int postStart, int postEnd) {
        if(inStart > inEnd){
            return NULL;
        }
        TreeNode* root = new TreeNode(postorder[postEnd]);
        int i = inStart;
        for (; i <= inEnd; i++) {
            if (inorder[i] == root->val) {
                break;
            }
        }
        int leftSize = i - inStart;
        int rightSize = inEnd - i;
        root->left = solve(inorder, postorder, inStart, i - 1, postStart,
                           postStart + leftSize - 1);
        root->right = solve(inorder, postorder, i + 1, inEnd,
                            postEnd - rightSize, postEnd - 1);
        return root;
    }
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int n = inorder.size();
        int inStart = 0;
        int inEnd = n - 1;
        int postStart = 0;
        int postEnd = n - 1;
        return solve(inorder, postorder, inStart, inEnd, postStart, postEnd);
    }
};