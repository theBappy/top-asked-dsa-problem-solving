class Codec {
    serialize(root){
        const res = []
        const dfs = (node) => {
            if(!node) {
                res.push("n")
                return
            }
            res.push(String(node.val))
            dfs(node.left)
            dfs(node.right)
        }
        dfs(root)
        return res.join(",")
    }
    desSerialize(data){
        const vals = data.split(",")
        this.i = 0
        const dfs = () => {
            if(vals[self.i] === 'n'){
                this.i += 1
                return null
            }
            const node = new TreeNode(parseInt(vals[this.i]))
            this.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        }
        return dfs()
    }
}