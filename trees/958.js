class Solution{
    countNodes(root){
        if(root === null){
            return 0
        }
        return 1 + this.countNodes(root.left) + this.countNodes(root.right)
    }
    dfs(root, i, totalNodes){
        if(root === null){
            return true
        }
        if(i > totalNodes){
            return false
        }
        return this.dfs(root.left, 2*i, totalNodes) && this.
        dfs(root.right, 2*i + 1, totalNodes)
    }
    isCompleteTree(root){
        const totalNodes = this.countNodes(root)
        const i = 1
        return this.dfs(root, i, totalNodes)
    }
}