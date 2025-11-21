

var isSymmetric = function (root) {
    const check = (l, r) => {
        if (l === null && r === null) {
            return true
        }
        if (l === null || r === null) {
            return false
        }
        if (l.val === r.val && check(l.left, r.right) && check(l.right, r.left)) {
            return true
        }
        return false
    }
    if (!root) {
        return true;
    }
    return check(root.left, root.right)
};