class Solution:
    def getLength(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.getLength(head)
        if length == n:
            return head.next
        travel = length - n
        temp = head
        prev = None
        while travel > 0:
            prev = temp
            temp = temp.next
            travel -= 1
        prev.next = temp.next
        return head



class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        for _ in range(n):
            temp = temp.next
        if temp is None:
            result = head.next
            return result
        prev = head
        while temp and temp.next:
            prev = prev.next
            temp = temp.next
        prev.next = prev.next.next
        return head