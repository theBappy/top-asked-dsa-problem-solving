class Solution {
    constructor(){
        this.result = 0
    }
    dfs(adj, curr, parent, s){
        let longest = 0
        let second_longest = 0
        for(const child of adj[curr]){
            if(child === parent){
                continue
            }
            const child_longest_length = this.dfs(adj, child, curr, s)
            if(s[child] === s[curr]){
                continue
            }
            if(child_longest_length > second_longest){
                second_longest = child_longest_length
            }
            if(second_longest > longest){
                longest, second_longest = second_longest, longest
            }
        }
        const largest_child = 1 + Math.max(longest, second_longest)
        const only_root = 1
        const largest_child_bottom = 1 + longest + second_longest
        this.result = Math.max(this.result, largest_child, only_root, largest_child_bottom)
        return Math.max(only_root, largest_child)
    }
    longestPath(parent, s){
        const n = parent.length
        const adj = new Map()
        for(let i = 1; i < n; i++){
            const u = i
            const v = parent[i]
            if(!adj.has(u)) adj.set(u, [])
            if(!adj.has(v)) adj.set(v, [])
            adj.get(u).push(v)
            adj.get(v).push(u)
        }
        this.dfs(adj, 0, -1, s)
        return this.result
    }
}