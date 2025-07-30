class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def fill(node, current_sum, current_path):
            if not node:
                return

            current_sum += node.val
            current_path.append(node.val)
            if not node.left and not node.right:
                if current_sum == targetSum:
                    result.append(list(current_path)) 
            else:
                fill(node.left, current_sum, current_path)
                fill(node.right, current_sum, current_path)

            current_path.pop()

        fill(root, 0, [])
        return result