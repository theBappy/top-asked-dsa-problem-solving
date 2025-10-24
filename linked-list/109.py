class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        slow = head
        fast = head
        slow_prev = head
        
        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next
        
        root = TreeNode(slow.val)
        
        slow_prev.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        
        return root
