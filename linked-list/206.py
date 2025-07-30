# Tc = O(n)
# Sc = Sc = (n) [due to recursion stack, each recursive call adds a new layer to the call stack]
class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last