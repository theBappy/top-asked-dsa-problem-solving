function isCyclicDFS(g, start, visited, parent){
    visited[start] = true
    for(const neighbor of g[start]){
        if(neighbor === parent) continue
        if(visited[neighbor]) return true
        if(isCyclicDFS(g, neighbor, visited, start))
            return true
    }
    return false
}


function isCyclic(g, V){
    const visited = new Array(V).fill(false)
    for(let i = 0; i < V; i++){
        if(!visited[i] && isCyclicDFS(g, i, visited, -1)){
            return true
        }
    }
    return false
}