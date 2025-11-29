function dfsRec(adj, visited, s, res){
    visited[s] = true
    res.push(s)
    for(let i of adj[s]){
        if(!visited[i]){
            dfsRec(adj, visited, i, res)
        }
    }
}

function dfs(adj){
    const visited = new Array(adj.length).fill(false)
    const res = []
    dfsRec(adj, visited, 0, res)
    return res
}