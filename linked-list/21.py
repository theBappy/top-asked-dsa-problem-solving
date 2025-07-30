# Tc = O(n+m) [length of two lists]
# Sc = (n+m) [due to recursion stack]
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
class Solution:
    def mergedTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            result = list1
            result.next = self.mergedTwoLists(list1.next, list2)
        else:
            result = list2
            result.next = self.mergedTwoLists(list1, list2.next)
        return result