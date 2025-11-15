var addOneRow = function (root, val, depth) {
    if (depth === 1) {
        const newRoot = new TreeNode(val);
        newRoot.left = root;
        return newRoot;
    }

    const add = (node, currentDepth) => {
        if (!node) return null;

        if (currentDepth === depth - 1) {
            const oldLeft = node.left;
            const oldRight = node.right;

            node.left = new TreeNode(val);
            node.right = new TreeNode(val);

            node.left.left = oldLeft;
            node.right.right = oldRight;

            return;
        }

        add(node.left, currentDepth + 1);
        add(node.right, currentDepth + 1);
    };

    add(root, 1);
    return root;
};
