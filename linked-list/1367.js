var isSubPath = function (head, root) {
    const check = function (head, root) {
        if (head === null) {
            return true;
        }
        if (root === null) {
            return false;
        }
        if (head.val !== root.val) {
            return false;
        }
        return check(head.next, root.left) || check(head.next, root.right);
    };
    
    if (root === null) {
        return false;
    }
    return check(head, root) || isSubPath(head, root.left) || isSubPath(head, root.right);
};
