class Solution {
    inorder(root, sum, targetSum) {
        if (root === null) {
            return false;
        }
        sum += root.val;
        if (root.left === null && root.right === null) {
            return sum === targetSum;
        }
        const leftSide = this.inorder(root.left, sum, targetSum);
        const rightSide = this.inorder(root.right, sum, targetSum);
        return leftSide || rightSide;
    }

    hasPathSum(root, targetSum) {
        let sum = 0;
        const result = this.inorder(root, sum, targetSum);
        return result;
    }
}