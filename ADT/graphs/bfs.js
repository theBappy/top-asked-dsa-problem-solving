function bfs(adj){
    const V = adj.length
    const visited = new Array(V).fill(false)
    const res = []
    const q = new Denque()
    let src = 0
    visited[src] = true
    q.push(src)

    while(!q.isEmpty()){
        const curr = q.shift()
        res.push(curr)

        for(const x of adj[curr]){
            if(!visited[x]){
                visited[x] = true
                q.push(x)
            }
        }
    }
    return res
}