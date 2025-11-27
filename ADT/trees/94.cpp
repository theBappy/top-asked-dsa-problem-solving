// Morris Traversal

// Tc = O(n)
// Sc = O(1) [not used recursion so system stack is not used but with recursion for system stack depth]

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        TreeNode* curr = root;
        while (curr != NULL) {
            if (curr->left == NULL) {
                result.push_back(curr->val);
                curr = curr->right;
            } else {
                TreeNode* leftChild = curr->left;
                
                while (leftChild->right != NULL) {
                    leftChild = leftChild->right;
                }
                
                leftChild->right = curr;
                TreeNode* temp = curr;
                curr = curr->left;
                temp->left = NULL;
            }
        }

        return result;
    }
};