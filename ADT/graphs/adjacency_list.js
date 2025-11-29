// adjacency matrix
function createGraph(V, edges){
    let mat = Array.from({length: V}, () => Array(V).fill(0))
    for(let it of edges){
        let u = it[0]
        let v = it[1]

        mat[u][v] = 1
        mat[v][u] = 1
    }
    return mat
}

function createGraph(V, edges){
    let mat = Array.from({length: V}, () => Array(V).fill(0))

    for(let it of edges){
        let u = it[0]
        let v = it[1]

        mat[u][v] = 1
    }
    return mat
}

function createGraph(V, edges){
    let adj = Array.from({length: V}, () => [])
    for(let it of edges){
        let u = it[0]
        let v = it[1]
        adj[u].push(v)
    }
    return adj
}

function createGraph(V, edges){
    let adj = Array.from({length: V}, () => [])
    for(let it of edges){
        let u = it[0]
        let v = it[1]
        adj[u].push(v)
    }
    return adj
}