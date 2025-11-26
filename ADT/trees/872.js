
var leafSimilar = function (root1, root2) {
    let s1 = []
    let s2 = []
    const inOrder = (node, s) => {
        if (!node)
            return;
        if (node.left === null && node.right === null) {
            s.push(node.val.toString() + "_")
            return
        }
        inOrder(node.left, s)
        inOrder(node.right, s)
    }
    inOrder(root1, s1)
    inOrder(root2, s2)
    return s1.join("") === s2.join("")
};