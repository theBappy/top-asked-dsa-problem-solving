class Solution {
    dfsFindMinChar(adj, currCh, visited){
        visited[currCh.charCodeAt(0) - 'a'.charCodeAt(0)] = 1
        let minChar = currCh
        for(const v of adj[currCh]){
            if(!visited[v.charCodeAt(0) - 'a'.charCodeAt(0)]){
                minChar = String.fromCharCode(Math.min(minChar.charCodeAt(0), this.dfsFindMinChar(adj, v, visited).charCodeAt(0)))
            }
        }
        return minChar
    }
    smallestEquivalentString(s1, s2, baseStr){
        const n = s1.length
        const m = s2.length
        const adj = {}
        for(let i = 0; i < n; i++){
            const u = s1[i]
            const v = s2[i]
            if(!adj.has(u)) adj[u] = []
            if(!adj.has(v)) adj[v] = []
            adj[u].push(v)
            adj[v].push(u)
        }
        let result = ''
        for(let i = 0; i < m; i++){
            const ch = baseStr[i]
            const visited = new Array(26).fill(false)
            const minChar = this.dfsFindMinChar(adj, ch, visited)
            result += minChar
        }
        return result
    }
}