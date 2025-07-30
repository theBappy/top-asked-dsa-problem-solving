class Solution{
    leverOrder(root){
        const res = []
        const q = []
        if(root) q.push(root)
        while(q.length > 0){
            const qLen = q.length
            const level = []
            for(let i = 0; i<qLen; i++){
                const node = q.shift()
                if(node){
                    level.push(node.val)
                    if(node.left) q.push(node.left)
                    if(node.right) q.push(node.right)
                }
            }
            if(level.length > 0){
                res.push(level)
            }
        }
        return res
    }
}