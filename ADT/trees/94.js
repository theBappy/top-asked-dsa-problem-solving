
var inorderTraversal = function (root) {
    const res = []
    let curr = root
    while (curr !== null) {
        if (curr.left === null) {
            res.push(curr.val)
            curr = curr.right
        } else {
            let leftChild = curr.left
            while (leftChild.right !== null) {
                leftChild = leftChild.right
            }
            leftChild.right = curr
            const temp = curr
            curr = curr.left
            temp.left = null
        }
    }
    return res
};