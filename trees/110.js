class Solution {
    isBalanced(root) {
        const dfs = (node) => {
            if (!node) return [true, 0];
            const [leftBalanced, leftHeight] = dfs(node.left);
            const [rightBalanced, rightHeight] = dfs(node.right);
            const balanced = leftBalanced && rightBalanced && Math.abs(leftHeight - rightHeight) <= 1;
            return [balanced, 1 + Math.max(leftHeight, rightHeight)];
        };
        return dfs(root)[0];
    }
}