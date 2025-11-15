// A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
// Tc = O(n)
// Sc = O(n + n) [for inorder + for construct] => O(n)
// For inplace -> DSW Algo(out of scope)


class Solution {
public:
    void inOrder(TreeNode* root, vector<int>& vec) {
        if (!root) {
            return;
        }
        inOrder(root->left, vec);
        vec.push_back(root->val);
        inOrder(root->right, vec);
    }
    TreeNode* constructBST(int l, int r, vector<int> vec) {
        if (l > r) {
            return NULL;
        }
        int mid = l + (r - l) / 2;
        TreeNode* root = new TreeNode(vec[mid]);
        root->left = constructBST(l, mid - 1, vec);
        root->right = constructBST(mid + 1, r, vec);

        return root;
    }
    TreeNode* balanceBST(TreeNode* root) {
        vector<int> vec;
        inOrder(root, vec);
        int l = 0;
        int r = vec.size() - 1;
        return constructBST(l, r, vec);
    }
};

