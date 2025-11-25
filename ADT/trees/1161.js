
var maxLevelSum = function (root) {
    let maxSum = Number.NEGATIVE_INFINITY
    let result_level = 0
    let q = []
    q.push(root)
    let curr_level = 1
    while (q.length) {
        let n = q.length
        let sum = 0
        for (let i = 0; i < n; i++) {
            let temp = q.shift()
            sum += temp.val
            if (temp.left) {
                q.push(temp.left)
            }
            if (temp.right) {
                q.push(temp.right)
            }
        }
        if (sum > maxSum) {
            maxSum = sum
            result_level = curr_level
        }
        curr_level++
    }
    return result_level
};



var maxLevelSum = function (root) {
    let mp = new Map();
    const dfs = (node, level) => {
        if (!node) {
            return;
        }
        mp.set(level, (mp.get(level) || 0) + node.val);
        dfs(node.left, level + 1);
        dfs(node.right, level + 1);
    };
    dfs(root, 1);
    let maxSum = Number.NEGATIVE_INFINITY;
    let result_level = 0;
    for (const [level, sum] of mp.entries()) {
        if (sum > maxSum) {
            maxSum = sum;
            result_level = level;
        }
    }
    return result_level;
};
