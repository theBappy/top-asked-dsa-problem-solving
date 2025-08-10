class Solution {
    primsAlgorithm(adj, V) {
        const minHeap = new MinPriorityQueue({ priority: (node) => node[0] });
        minHeap.enqueue([0, 0]); // [weight, node]
        const inMST = new Array(V).fill(false);
        let sum = 0;
        let nodesProcessed = 0;

        while (!minHeap.isEmpty() && nodesProcessed < V) {
            const [wt, node] = minHeap.dequeue().element;
            
            if (inMST[node]) continue;
            
            inMST[node] = true;
            sum += wt;
            nodesProcessed++;
            
            for (const [neighbor, neighborWt] of adj[node]) {
                if (!inMST[neighbor]) {
                    minHeap.enqueue([neighborWt, neighbor]);
                }
            }
        }
        
        return sum;
    }

    minCostConnectPoints(points) {
        const V = points.length;
        const adj = Array.from({ length: V }, () => []);
        
        for (let i = 0; i < V; i++) {
            for (let j = i + 1; j < V; j++) {
                const [x1, y1] = points[i];
                const [x2, y2] = points[j];
                const d = Math.abs(x1 - x2) + Math.abs(y1 - y2);
                adj[i].push([j, d]);
                adj[j].push([i, d]);
            }
        }
        
        return this.primsAlgorithm(adj, V);
    }
}

// Helper MinPriorityQueue implementation (using a simple array for small graphs)
class MinPriorityQueue {
    constructor({ priority }) {
        this.heap = [];
        this.priority = priority;
    }
    
    enqueue(item) {
        this.heap.push(item);
        this.heap.sort((a, b) => this.priority(a) - this.priority(b));
    }
    
    dequeue() {
        return { element: this.heap.shift() };
    }
    
    isEmpty() {
        return this.heap.length === 0;
    }
}

// Example usage
const sol = new Solution();
const points = [[0,0],[2,2],[3,10],[5,2],[7,0]];
console.log(sol.minCostConnectPoints(points)); // Output: 20
