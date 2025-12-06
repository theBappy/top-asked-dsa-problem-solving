var minTime = function (n, edges, hasApple) {
    const adj = new Map();

    for (const [u, v] of edges) {
        if (!adj.has(u)) adj.set(u, []);
        if (!adj.has(v)) adj.set(v, []);
        adj.get(u).push(v);
        adj.get(v).push(u);
    }

    const DFS = (node, parent) => {
        let time = 0;

        for (const child of adj.get(node) || []) {
            if (child === parent) continue;

            const childTime = DFS(child, node);

            if (childTime > 0 || hasApple[child]) {
                time += childTime + 2;  
            }
        }
        return time;
    };

    return DFS(0, -1);
};
