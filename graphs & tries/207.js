class Solution{
    isCycleDFS(adj, u, visited, inRecursion){
        visited[u] = true
        inRecursion[u] = true
        for(let v of adj[u]){
            if(!visited[v] && this.isCycleDFS(adj, v, visited, inRecursion)){
                return true
            }
            else if(inRecursion[v]){
                return true
            }
        }
        inRecursion[u] = false
        return false
    }
    canFinish(numCourses, prerequisites){
        const adj = Array.from({length: numCourses}, () =>[])
        const visited = new Array(numCourses).fill(false)
        const inRecursion = new Array(numCourses).fill(false)
        for(let [a,b] of prerequisites){
            adj[b].push(a)
        }
        for(let i = 0; i <numCourses; i++){
            if(!visited[i] && this.isCycleDFS(adj, i, visited, inRecursion)){
                return false
            }
        }
        return true
    }
}