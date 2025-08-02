/**
 * @param {number} n
 * @param {number[][]} dislikes
 * @return {boolean}
 */
class Solution {
    /**
     * Performs a Breadth-First Search (BFS) to check if the connected component
     * starting from 'startNode' is bipartite.
     * @param {Map<number, number[]>} adj
     * @param {number} startNode
     * @param {number[]} color
     * @return {boolean}
     */
    bfsCheckBipartite(adj, startNode, color) {
        const queue = [startNode];
        // We use 0 and 1 for colors. 0 is one group, 1 is the other.
        // -1 indicates an uncolored node.
        color[startNode] = 0;

        while (queue.length > 0) {
            const u = queue.shift();

            if (adj.has(u)) {
                for (const v of adj.get(u)) {
                    if (color[v] === -1) {
                        // If neighbor is uncolored, give it the opposite color
                        color[v] = 1 - color[u];
                        queue.push(v);
                    } else if (color[v] === color[u]) {
                        // If neighbor has the same color, we found an odd-length cycle
                        return false;
                    }
                }
            }
        }
        return true;
    }

    /**
     * Determines if a group of n people can be divided into two groups
     * such that no two people who dislike each other are in the same group.
     * This is equivalent to checking if the graph is bipartite.
     * @param {number} n
     * @param {number[][]} dislikes
     * @return {boolean}
     */
    possibleBipartition(n, dislikes) {
        // Build the adjacency list representation of the graph
        const adj = new Map();
        for (let i = 1; i <= n; i++) {
            adj.set(i, []);
        }
        for (const [u, v] of dislikes) {
            adj.get(u).push(v);
            adj.get(v).push(u);
        }

        // Initialize a color array for each person (1 to n).
        // -1 means uncolored, 0 and 1 are the two groups.
        const color = new Array(n + 1).fill(-1);

        // Iterate through all people to handle disconnected components of the graph
        for (let i = 1; i <= n; i++) {
            if (color[i] === -1) {
                // If a person is uncolored, start a BFS from them
                if (!this.bfsCheckBipartite(adj, i, color)) {
                    // If any connected component is not bipartite, the whole graph isn't
                    return false;
                }
            }
        }

        return true;
    }
}