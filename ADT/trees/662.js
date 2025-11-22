
var widthOfBinaryTree = function (root) {
    if (!root) return 0;
    const que = [];
    que.push({ node: root, index: 0n });
    let maxWidth = 0n;

    while (que.length > 0) {
        const n = que.length;
        const f = que[0].index;
        const l = que[que.length - 1].index;
        maxWidth = maxWidth > (l - f + 1n) ? maxWidth : (l - f + 1n);

        for (let i = 0; i < n; i++) {
            const { node: curr, index: d } = que.shift();
            if (curr.left) {
                que.push({ node: curr.left, index: 2n * d + 1n });
            }
            if (curr.right) {
                que.push({ node: curr.right, index: 2n * d + 2n });
            }
        }
    }
    return Number(maxWidth);
};