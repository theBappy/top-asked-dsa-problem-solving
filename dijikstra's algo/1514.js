class MaxHeap{
    constructor(){
        this.heap =[]
    }
    push(value, priority){
        this.heap.push({value, priority})
        this.heap.sort((a, b) => b.priority - a.priority)
    }
    pop(){
        return this.heap.shift()
    }
    isEmpty(){
        return this.heap.length === 0
    }
}
function maxProbability(n, edges, succProb, start, end){
    const adj = Array.from({length: n}, () => [])
    edges.forEach(([u, v]) =>{
        adj[u].push([v, succProb[i]])
        adj[v].push([u, succProb[i]])
    })
    const result = new Array(n).fill(0.0)
    result[start] = 1.0
    const maxHeap = new MaxHeap()
    maxHeap.push(start, 1.0)
    while(!maxHeap.isEmpty()){
        const {value: currNode, priority: currProb} = maxHeap.pop()
        if(currNode === end) return currProb
        for(const [adjNode, adjProb] of adj[currNode]){
            const newProb = currProb * adjProb
            if(newProb > result[adjNode]){
                result[adjNode] = newProb
                maxHeap.push(adjNode, newProb)
            }
        }
    }
    return 0.0
}