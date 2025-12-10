// Tc = O(E α(V)) =~ O(V+E)
// Where α(V) is the inverse Ackermann function → grows extremely slowly
// (for all practical purposes ≤ 4).


/**
 * @param {string[]} equations
 * @return {boolean}
 */
var equationsPossible = function(equations) {
    const parent = new Array(26).fill(0).map((_, i) => i);
    const rank = new Array(26).fill(1);

    const find = (x) => {
        if (parent[x] !== x) {
            parent[x] = find(parent[x]);  // path compression
        }
        return parent[x];
    };

    const union = (x, y) => {
        const px = find(x);
        const py = find(y);
        if (px !== py) {
            if (rank[px] > rank[py]) {
                parent[py] = px;
            } else if (rank[px] < rank[py]) {
                parent[px] = py;
            } else {
                parent[px] = py;
                rank[py] += 1;
            }
        }
    };

    // First process all "==" equations
    for (const eq of equations) {
        if (eq[1] === "=") {
            const a = eq.charCodeAt(0) - 97;
            const b = eq.charCodeAt(3) - 97;
            union(a, b);
        }
    }

    // Then process all "!=" equations
    for (const eq of equations) {
        if (eq[1] === "!") {
            const a = eq.charCodeAt(0) - 97;
            const b = eq.charCodeAt(3) - 97;
            if (find(a) === find(b)) {
                return false;
            }
        }
    }

    return true;
};
