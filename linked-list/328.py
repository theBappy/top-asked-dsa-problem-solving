# Tc = O(n)
# Sc = O(1)
class Solution:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            even.next = even.next.next

            odd = odd.next
            even = even.next
        odd.next = even_head
        return head