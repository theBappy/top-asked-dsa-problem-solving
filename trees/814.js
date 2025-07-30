class Solution {
    pruneTree(root) {
        if (root === null) {
            return null;
        }
        root.left = this.pruneTree(root.left);
        root.right = this.pruneTree(root.right);
        if (root.left === null && root.right === null && root.val === 0) {
            return null;
        }
        return root;
    }
}