class Solution {
    lowestCommonAncestor(root, p, q) {
        if (root === null) {
            return null;
        }
        if (root === p || root === q) {
            return root;
        }
        const leftN = this.lowestCommonAncestor(root.left, p, q);
        const rightN = this.lowestCommonAncestor(root.right, p, q);
        if (leftN !== null && rightN !== null) {
            return root;
        }
        if (leftN !== null) {
            return leftN;
        }
        return rightN;
    }
}