
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode(0)
        large = ListNode(0)
        smallP = small
        largeP = large
        while head:
            if head.val < x:
                smallP.next = head
                smallP = smallP.next
            else:
                largeP.next = head
                largeP = largeP.next
            head = head.next
        smallP.next = large.next
        largeP.next = None
        return small.next