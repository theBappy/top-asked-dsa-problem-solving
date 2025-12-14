class Solution {
    constructor() {
        this.dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]];
    }

    minimumEffortPath(heights) {
        const m = heights.length;
        const n = heights[0].length;

        const isSafe = (x, y) => x >= 0 && x < m && y >= 0 && y < n;

        const result = Array.from({ length: m }, () => Array(n).fill(Number.MAX_SAFE_INTEGER));

        // Min heap implementation using a priority queue
        class MinHeap {
            constructor() {
                this.heap = [];
            }

            push(val) {
                this.heap.push(val);
                this._bubbleUp(this.heap.length - 1);
            }

            pop() {
                if (this.heap.length === 1) return this.heap.pop();
                const top = this.heap[0];
                this.heap[0] = this.heap.pop();
                this._bubbleDown(0);
                return top;
            }

            top() {
                return this.heap[0];
            }

            empty() {
                return this.heap.length === 0;
            }

            _bubbleUp(index) {
                while (index > 0) {
                    let parent = Math.floor((index - 1) / 2);
                    if (this.heap[parent][0] <= this.heap[index][0]) break;
                    [this.heap[parent], this.heap[index]] = [this.heap[index], this.heap[parent]];
                    index = parent;
                }
            }

            _bubbleDown(index) {
                const length = this.heap.length;
                while (true) {
                    let left = 2 * index + 1;
                    let right = 2 * index + 2;
                    let smallest = index;

                    if (left < length && this.heap[left][0] < this.heap[smallest][0]) {
                        smallest = left;
                    }
                    if (right < length && this.heap[right][0] < this.heap[smallest][0]) {
                        smallest = right;
                    }
                    if (smallest === index) break;
                    [this.heap[smallest], this.heap[index]] = [this.heap[index], this.heap[smallest]];
                    index = smallest;
                }
            }
        }

        const pq = new MinHeap();
        pq.push([0, [0, 0]]);
        result[0][0] = 0;

        while (!pq.empty()) {
            const [diff, node] = pq.pop();
            const [x, y] = node;

            if (x === m - 1 && y === n - 1) return diff;

            for (const dir of this.dirs) {
                const x_ = x + dir[0];
                const y_ = y + dir[1];

                if (isSafe(x_, y_)) {
                    const newDiff = Math.max(diff, Math.abs(heights[x][y] - heights[x_][y_]));
                    if (result[x_][y_] > newDiff) {
                        result[x_][y_] = newDiff;
                        pq.push([newDiff, [x_, y_]]);
                    }
                }
            }
        }

        return result[m - 1][n - 1];
    }
}