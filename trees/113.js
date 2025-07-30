class Solution{
    pathSum(root, targetSum){
        const result = []
        const fill = (node, currentSum, currentPath) => {
            if(!node) return
            currentSum += node.val
            currentPath.push(node.val)
            if(!node.left && !node.right){
                if(currentSum === targetSum){
                    result.push([...currentPath])
                }
            }else{
                fill(node.left, currentSum, currentPath)
                fill(node.right, currentSum, currentPath)
            }
            currentPath.pop()
        }
        fill(root, 0, [])
        return result
    }
}