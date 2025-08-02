class Solution {
    dfs(rooms, source, visited){
        visited[source] = true
        for(let node of rooms[source]){
            if(!visited[node]){
                this.dfs(rooms, node, visited)
            }
        }
    }
    canVisitAllRooms(rooms){
        const n = rooms.length
        const visited = new Array(n).fill(false)
        this.dfs(rooms, 0, visited)
        for(let x of visited){
            if(!x){
                return false
            }
        }
        return true
    }
}