
var findMode = function (root) {
    let mp = new Map()
    const dfs = (root) => {
        if (!root) {
            return
        }
        dfs(root.left)
        mp.set(root.val, (mp.get(root.val) || 0) + 1)
        dfs(root.right)
    }
    dfs(root)
    const result = []
    let maxFreq = 0
    for (const [key, value] of mp.entries()) {
        if (value > maxFreq) {
            maxFreq = value
            result.length = 0
            result.push(key)
        } else if (value === maxFreq) {
            result.push(key)
        }
    }
    return result
};



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
 * @return {number[]}
 */
var findMode = function (root) {
    let currNum = 0
    let currFreq = 0
    let maxFreq = 0
    let result = []
    const dfs = (root) => {
        if (!root) {
            return
        }
        dfs(root.left)
        if (root.val === currNum) {
            currFreq++
        } else {
            currNum = root.val
            currFreq = 1
        }
        if (currFreq > maxFreq) {
            result = []
            maxFreq = currFreq
        }
        if (currFreq === maxFreq) {
            result.push(root.val)
        }
        dfs(root.right)
    }
    dfs(root)
    return result
};