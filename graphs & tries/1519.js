class Solution {
    dfs(adj, curr ,parent, result, labels, count){
        const myLabel = labels[curr]
        const countBeforeVisitingChild = count[myLabel.charCodeAt(0) - 'a'.charCodeAt(0)]
        count[myLabel.charCodeAt(0) - 'a'.charCodeAt(0)] += 1
        for(const v of adj[curr]){
            if(v === parent){
                continue
            }
            this.dfs(adj, v, curr, result, labels, count)
        }
        const countAfterVisitingChild = count[myLabel.charCodeAt(0) - 'a'.charCodeAt(0)]
        result[curr] = countAfterVisitingChild - countBeforeVisitingChild
    }
    countSubTress(n, edges, labels){
        const adj = Array.from({length: n}, () =>[])
        for(const [u, v] of edges){
            adj[u].push(v)
            adj[v].push(u)
        }
        const result = new Array(n).fill(0)
        const count = new Array(26).fill(0)
        this.dfs(adj, 0, -1, result, labels, count)
        return result
    }

}