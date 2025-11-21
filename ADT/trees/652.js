var findDuplicateSubtrees = function (root) {
    const dfs = (node, mp, res) => {
        if (node === null) {
            return "Null";
        }
        const s = node.val + "," + dfs(node.left, mp, res) + "," + dfs(node.right, mp, res);
        if (mp.has(s) && mp.get(s) === 1) {
            res.push(node);
        }
        mp.set(s, (mp.get(s) || 0) + 1);
        return s;
    };
    const mp = new Map();
    const res = [];
    dfs(root, mp, res);
    return res;
};
