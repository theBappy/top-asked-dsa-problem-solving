// By Prim's Algorithm
// Tc = O(E*(logE + logE) => O(ElogE)
//“Lazy Prim’s runs in O(E log E), which simplifies to O(E log V) since E ≤ V².”

class MinHeap {
    constructor() {
        this.heap = [];
    }

    push(item) {
        this.heap.push(item);
        this._up(this.heap.length - 1);
    }

    pop() {
        if (this.heap.length === 1) return this.heap.pop();
        const top = this.heap[0];
        this.heap[0] = this.heap.pop();
        this._down(0);
        return top;
    }

    _up(i) {
        while (i > 0) {
            let p = Math.floor((i - 1) / 2);
            if (this.heap[p][0] <= this.heap[i][0]) break;
            [this.heap[p], this.heap[i]] = [this.heap[i], this.heap[p]];
            i = p;
        }
    }

    _down(i) {
        const n = this.heap.length;
        while (true) {
            let smallest = i;
            let l = 2 * i + 1;
            let r = 2 * i + 2;

            if (l < n && this.heap[l][0] < this.heap[smallest][0])
                smallest = l;
            if (r < n && this.heap[r][0] < this.heap[smallest][0])
                smallest = r;

            if (smallest === i) break;
            [this.heap[i], this.heap[smallest]] = [this.heap[smallest], this.heap[i]];
            i = smallest;
        }
    }

    isEmpty() {
        return this.heap.length === 0;
    }
}

class Solution {
    spanningTree(V, adj) {
        // Min-heap storing [weight, node]
        const heap = new MinHeap();
        heap.push([0, 0]); // Start from node 0

        const inMST = new Array(V).fill(false);
        let sum = 0;

        while (!heap.isEmpty()) {
            const [wt, node] = heap.pop();

            // Skip if already in MST
            if (inMST[node]) continue;

            // Include node
            inMST[node] = true;
            sum += wt;

            // Push adjacent edges
            for (const [neighbor, neighborWt] of adj[node]) {
                if (!inMST[neighbor]) {
                    heap.push([neighborWt, neighbor]);
                }
            }
        }

        return sum;
    }
}
