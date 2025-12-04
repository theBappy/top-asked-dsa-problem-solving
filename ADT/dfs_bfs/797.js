/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function (graph) {
    const dfs = (start, target, result, temp) => {
        temp.push(start)
        if (start === target) {
            result.push([...temp])
        } else {
            for (const v of graph[start]) {
                dfs(v, target, result, temp)
            }
        }
        temp.pop()
    }
    const n = graph.length
    const source = 0
    const target = n - 1
    const result = []
    const temp = []
    dfs(source, target, result, temp)
    return result
};