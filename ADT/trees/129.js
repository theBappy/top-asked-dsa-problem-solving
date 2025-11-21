var sumNumbers = function (root) {
    const find = (node, curr) => {
        if (!node) {
            return 0;
        }
        curr = curr * 10 + node.val;
        if (node.left === null && node.right === null) {
            return curr;
        }
        const left_sum = find(node.left, curr);
        const right_sum = find(node.right, curr);
        return left_sum + right_sum;
    };
    return find(root, 0);
};
