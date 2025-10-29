
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        left = None
        right = list1
        for i in range(b+1):
            if i == a - 1:
                left = right
            right = right.next
        left.next = list2
        temp = list2
        while temp.next:
            temp = temp.next
        temp.next = right
        return list1