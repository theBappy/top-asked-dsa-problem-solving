/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var longestZigZag = function (root) {
    let maxPath = 0
    function solve(node, steps, goLeft) {
        if (!node) return
        maxPath = Math.max(maxPath, steps)
        if (goLeft) {
            solve(node.left, steps + 1, false)
            solve(node.right, 1, true)
        } else {
            solve(node.right, steps + 1, true)
            solve(node.left, 1, false)
        }
    }
    if (!root) return 0
    solve(root, 0, true)
    solve(root, 0, false)
    return maxPath
};