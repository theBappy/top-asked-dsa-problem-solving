var distanceK = function (root, target, k) {
    const result = [];
    const parent = new Map();

    // Build parent map
    const addParent = (node) => {
        if (!node) return;
        if (node.left) {
            parent.set(node.left, node);
            addParent(node.left);
        }
        if (node.right) {
            parent.set(node.right, node);
            addParent(node.right);
        }
    };

    const kDistanceNodes = (target, k, result) => {
        const q = [target];
        const visited = new Set([target]);

        while (q.length > 0) {
            let n = q.length;

            if (k === 0) break;

            while (n--) {
                const curr = q.shift();

                if (curr.left && !visited.has(curr.left)) {
                    q.push(curr.left);
                    visited.add(curr.left);
                }
                if (curr.right && !visited.has(curr.right)) {
                    q.push(curr.right);
                    visited.add(curr.right);
                }
                if (parent.has(curr) && !visited.has(parent.get(curr))) {
                    q.push(parent.get(curr));
                    visited.add(parent.get(curr));
                }
            }
            k--;
        }

        while (q.length > 0) {
            result.push(q.shift().val);
        }
    };

    addParent(root);
    kDistanceNodes(target, k, result);
    return result;
};
