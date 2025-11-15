var bstToGst = function(root) {
    const solve = (node, sum) => {
        if (!node) return;

        solve(node.right, sum);
        sum.value += node.val;
        node.val = sum.value;
        solve(node.left, sum);
    }

    let sum = { value: 0 };
    solve(root, sum);
    return root;
};
