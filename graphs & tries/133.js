
var cloneGraph = function(node) {
    if(!node) return null
    const mp = new Map()
    function dfs(originalNode){
        if(mp.has(originalNode)){
            return mp.get(originalNode)
        }
        const clone = new Node(originalNode.val)
        mp.set(originalNode, clone)
        for(const neighbor of originalNode.neighbors){
            clone.neighbors.push(dfs(neighbor))
        }
        return clone
    }
    return dfs(node)
};