class Solution{
    solve(root, result){
        if(root === null){
            return 0
        }
        const left = this.solve(root.left, result)
        const right = this.solve(root.right, result)
        result[0] = Math.max(result[0], left + right)
        return max(left, right) + 1
    }
    diameterOfBinaryTree(root){
        if(root === null){
            return 0
        }
        const result = [Number.NEGATIVE_INFINITY]
        this.solve(root,result)
        return result[0]
    }
}