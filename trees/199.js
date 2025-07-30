class TreeNode {
    constructor(val=0, left=null, right= null){
        this.val = val
        this.left = left
        this.right = right
    }
}
function rightSideView(root){
    if(!root) return []
    result = []
    const queue = [root]
    while(queue.length >0){
        const levelSize = queue.length
        let rightNode = null
        for(let i = 0; i<levelSize; i++){
            rightNode = queue.shift()
            if(rightNode.left) queue.push(rightNode.left)
            if(rightNode.right) queue.push(rightNode.right)
        }
    if(rightNode){
        result.push(rightNode.val)
    }
    }
    return result
}


// Pre-Order traversal(DFS)
class Solution{
    preOrder(root, level, result){
        if(root === null)
            return;
        if(result.length < level){
            result.push(root.val)
        }
        this.preOrder(root.right, level + 1,result)
        this.preOrder(root.left, level + 1, result)
    }
    rightSideView(root){
        const result = []
        this.preOrder(root, 1, result)
        return result
    }
}