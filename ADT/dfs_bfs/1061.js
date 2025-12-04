// Using DFS
//T.C : O(m* (V+E)), we try DFS m times
//S.C : O(V+E)
var smallestEquivalentString = function(s1, s2, baseStr) {
    const DFSFindMinChar = (adj, curr_ch, visited) => {
        const idx = curr_ch.charCodeAt(0) - 'a'.charCodeAt(0);
        if (visited[idx]) return curr_ch;
        visited[idx] = 1;
        let minChar = curr_ch;
        for (const v of (adj.get(curr_ch) || [])) {
            const candidate = DFSFindMinChar(adj, v, visited);
            if (candidate < minChar) minChar = candidate;
        }
        return minChar;
    }

    const n = s1.length;
    const adj = new Map();

    for (let i = 0; i < n; i++) {
        const u = s1[i], v = s2[i];
        if (!adj.has(u)) adj.set(u, []);
        if (!adj.has(v)) adj.set(v, []);
        adj.get(u).push(v);
        adj.get(v).push(u);
    }

    let result = '';
    for (const ch of baseStr) {
        const visited = new Array(26).fill(0);
        result += DFSFindMinChar(adj, ch, visited);
    }

    return result;
};
