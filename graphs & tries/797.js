class Solution{
    dfs(graph, u, target, res, temp){
        temp.push(u)
        if(u === target){
            res.push([...temp])
        }else{
            for(let v of graph[u]){
                this.dfs(graph, v, target, res, temp)
            }
        }
        temp.pop()
    }
    allPathsSourceTarget(graph){
        const n = graph.length
        const source = 0
        const res = []
        const temp = []
        const target = n - 1
        this.dfs(graph, source, target, res, temp)
        return res
    }
}