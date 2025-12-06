// Meta

var minReorder = function(n, connections) {
    const adj = new Map();

    // Build adjacency list: store [neighbor, isOriginalDirection]
    for (const [a, b] of connections) {
        if (!adj.has(a)) adj.set(a, []);
        if (!adj.has(b)) adj.set(b, []);

        adj.get(a).push([b, 1]); // original direction a → b
        adj.get(b).push([a, 0]); // opposite direction b → a
    }

    let edgesToReverse = 0;

    const dfs = (node, parent) => {
        for (const [nextNode, isOriginalDirection] of adj.get(node)) {
            if (nextNode === parent) continue;

            // If edge goes away from 0, we need to reverse it
            if (isOriginalDirection === 1) {
                edgesToReverse++;
            }

            dfs(nextNode, node);
        }
    };

    dfs(0, -1);
    return edgesToReverse;
};
