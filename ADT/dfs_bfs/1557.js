/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var findSmallestSetOfVertices = function (n, edges) {
    const indegree = new Array(n).fill(false)
    for(const edge of edges){
        const u = edge[0]
        const v = edge[1]
        indegree[v] = true
    }
    const result = []
    for(let i = 0; i < n; i++){
        if(!indegree[i]){
            result.push(i)
        }
    }
    return result
};