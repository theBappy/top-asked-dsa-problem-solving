
class Solution:
    def findLength(self, head: ListNode) -> int:
        l = 0 
        while head:
            head = head.next
            l += 1
        return l
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        Length = self.findLength(head)
        k_1 = k
        temp1 = head
        while k_1 > 1:
            temp1 = temp1.next
            k_1 -= 1
        k_2 =  Length - k + 1
        temp2 = head
        while k_2 > 1:
            temp2 = temp2.next
            k_2 -= 1
        temp1.val, temp2.val = temp2.val, temp1.val
        return head


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p1 = None
        p2 = None
        temp = head
        while temp is not None:
            if p2 is not None:
                p2 = p2.next
            k -= 1
            if k == 0:
                p1 = temp
                p2 = head
            temp = temp.next
        p1.val, p2.val = p2.val, p1.val
        return head
