
var countNodes = function (root) {
    if (!root)
        return 0
    const leftHeight = (node) => {
        if (!node)
            return 0
        let lh = 0
        let temp = root
        while (temp) {
            temp = temp.left
            lh++
        }
        return lh
    }
    const rightHeight = (node) => {
        if (!node)
            return 0
        let rh = 0
        let temp = root
        while (temp) {
            temp = temp.right
            rh++
        }
        return rh
    }
    const lh = leftHeight(root)
    const rh = rightHeight(root)
    if (lh === rh)
        return Math.pow(2, lh) - 1
    return 1 + countNodes(root.left) + countNodes(root.right)
};