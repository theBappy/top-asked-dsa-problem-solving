class Solution{
    constructor(val = 0, left = null, right = null){
        this.val = val
        this.left = left
        this.right = right
    }
}
class Solution{
    check(l, r){
        if(!l && !r){
            return true
        }
        if(!l || !r){
            return false
        }
        return (l.val === r.val) && this.check(l.left, r.right) && this.check(l.right === r.left)
    }
    isSymmetric(root){
        if(!root) return true;
        return this.check(root.left, root.right)
    }
}