class Solution {
    dfs(adj, curr, parent, hasApple){
        let time = 0
        for(const child of adj[curr]){
            if(child === parent) continue;
            const timeFromChild = this.dfs(adj, child,curr, hasApple)
            if(timeFromChild > 0 || hasApple[child]){
                time += 2 + timeFromChild
            }
        }
        return time
    }
    minTime(n, edges, hasApple){
        const adj = Array.from({length: n}, () =>[])
        for(const [u, v] of edges){
            adj[u].push(v)
            adj[v].push(u)
        }
        return this.dfs(adj, 0, -1, hasApple)
    }
}