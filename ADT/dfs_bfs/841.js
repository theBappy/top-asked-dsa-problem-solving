/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function (rooms) {
    const dfs = (source, visited) => {
        visited[source] = true
        for (const node of rooms[source]) {
            if (!visited[node]) {
                dfs(node, visited)
            }
        }
    }
    const n = rooms.length
    const visited = new Array(n).fill(false)
    dfs(0, visited)
    return visited.every(v => v)
};