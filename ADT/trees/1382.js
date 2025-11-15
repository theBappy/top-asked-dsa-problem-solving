var balanceBST = function (root) {
    const vec = [];

    const inOrder = (node) => {
        if (!node) return;
        inOrder(node.left);
        vec.push(node.val);
        inOrder(node.right);
    };

    inOrder(root); 

    const constructBST = (l, r) => {
        if (l > r) return null;

        const mid = Math.floor((l + r) / 2);
        const node = new TreeNode(vec[mid]);

        node.left = constructBST(l, mid - 1);
        node.right = constructBST(mid + 1, r);

        return node;
    };

    return constructBST(0, vec.length - 1);
};
