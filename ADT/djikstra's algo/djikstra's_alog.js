class Solution {
    dijkstra(V, edges, src) {
        /**
         * Dijkstra's algorithm using adjacency list and min-heap.
         * V = number of vertices
         * edges = array of [u, v, w]
         * src = starting node
         */

        // Build adjacency list
        const adj = Array.from({ length: V }, () => []);
        for (const [u, v, w] of edges) {
            adj[u].push([v, w]);
            // adj[v].push([u, w]); // Uncomment for undirected graph
        }

        // Min-heap using priority queue implementation
        class MinHeap {
            constructor() {
                this.heap = [];
            }

            push(val) {
                this.heap.push(val);
                this._bubbleUp();
            }

            pop() {
                if (this.heap.length === 1) return this.heap.pop();
                const top = this.heap[0];
                this.heap[0] = this.heap.pop();
                this._bubbleDown();
                return top;
            }

            _bubbleUp() {
                let idx = this.heap.length - 1;
                while (idx > 0) {
                    let parent = Math.floor((idx - 1) / 2);
                    if (this.heap[parent][0] <= this.heap[idx][0]) break;
                    [this.heap[parent], this.heap[idx]] = [this.heap[idx], this.heap[parent]];
                    idx = parent;
                }
            }

            _bubbleDown() {
                let idx = 0;
                let length = this.heap.length;

                while (true) {
                    let left = 2 * idx + 1;
                    let right = 2 * idx + 2;
                    let smallest = idx;

                    if (left < length && this.heap[left][0] < this.heap[smallest][0]) {
                        smallest = left;
                    }
                    if (right < length && this.heap[right][0] < this.heap[smallest][0]) {
                        smallest = right;
                    }
                    if (smallest === idx) break;

                    [this.heap[idx], this.heap[smallest]] = [this.heap[smallest], this.heap[idx]];
                    idx = smallest;
                }
            }

            isEmpty() {
                return this.heap.length === 0;
            }
        }

        // Priority queue
        const pq = new MinHeap();
        pq.push([0, src]); // [distance, node]

        // Distance array
        const dist = Array(V).fill(Infinity);
        dist[src] = 0;

        while (!pq.isEmpty()) {
            const [d, node] = pq.pop();

            // Skip outdated entries
            if (d > dist[node]) continue;

            // Explore neighbors
            for (const [adjNode, wt] of adj[node]) {
                if (d + wt < dist[adjNode]) {
                    dist[adjNode] = d + wt;
                    pq.push([dist[adjNode], adjNode]);
                }
            }
        }

        return dist;
    }
}


// Dijkstra using Red-Black Tree
const { RBTree } = require("bintrees");

class Solution {
    dijkstra(V, edges, src) {
        // Build adjacency list
        const adj = Array.from({ length: V }, () => []);
        for (const [u, v, w] of edges) {
            adj[u].push([v, w]);
            // adj[v].push([u, w]);  // for undirected
        }

        // RBTree that stores (distance, node)
        const tree = new RBTree((a, b) =>
            a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]
        );

        const dist = Array(V).fill(Infinity);
        dist[src] = 0;

        tree.insert([0, src]);

        while (!tree.isEmpty()) {
            // Extract min (first)
            const [d, node] = tree.min();
            tree.remove([d, node]);

            // Explore neighbors
            for (const [adjNode, wt] of adj[node]) {
                if (d + wt < dist[adjNode]) {

                    // Remove old pair if present
                    if (dist[adjNode] !== Infinity) {
                        tree.remove([dist[adjNode], adjNode]);
                    }

                    // Update and insert new pair
                    dist[adjNode] = d + wt;
                    tree.insert([dist[adjNode], adjNode]);
                }
            }
        }

        return dist;
    }
}
