class TreeNode{
    constructor(val=0, left= null, right=null){
        this.val = val
        this.left = left
        this.right = right
    }
}
class Solution{
    deleteHelper(root, to_delete_set, result){
        if(!root) return null;
        root.left = this.deleteHelper(root.left, to_delete_set, result)
        root.right = this.deleteHelper(root.right, to_delete_set, result)
        if(to_delete_set.has(root.val)){
            if(root.left) result.push(root.left)
            if(root.right) result.push(root.right)
            return null
        }
        return root
    }
    delNodes(root, to_delete){
        const result = []
        const to_delete_set = new Set(to_delete)
        root = this.deleteHelper(root, to_delete_set, result)
        if(root) result.push(root)
        return result
    }
}