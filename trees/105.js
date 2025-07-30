function TreeNode(val, left, right){
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}
class Solution{
    constructor(){
        this.preorder_idx = 0
    }
    buildTree(preorder, inorder){
        const inorderMap = new Map()
        for(let i = 0; i < inorder.length ; i++){
            inorderMap.set(inorder[i], i)
        }
        this.preorder_idx = 0
        const solve = (start, end) => {
            if(start > end){
                return null
            }
            const rootVal = preorder[this.preorder_idx]
            this.preorder_idx++
            const root = new TreeNode(rootVal)
            const rootIndorderIdx = inorderMap.get(rootVal)
            root.left = solve(start, rootIndorderIdx -1)
            root.right = solve(rootIndorderIdx + 1, end)
            return root
        }
        const n = preorder.length
        return solve(0, n-1)
    }
}