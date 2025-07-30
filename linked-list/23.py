# Tc = O(n*logk)
# Sc = O(n)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoSortedLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: return l2
        if l2 is None: return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoSortedLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoSortedLists(l1, l2.next)

    def partitionAndMerge(self, start: int, end: int,  lists[ListNode]) -> ListNode:
        if start == end: return list[start]
        if start > end: return None
        mid = start + (end - start) // 2
        l1 = self.partitionAndMerge(start, mid, lists)
        l2 = self.partitionAndMerge(mid+1, end, lists)
        return self.mergeTwoSortedLists(l1, l2)
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        k = len(lists)
        if k == 0: return None
        return self.partitionAndMerge(0, k-1, lists)