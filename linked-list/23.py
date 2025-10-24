from typing import List, Optional


class Solution:
    def mergeTwoSortedLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoSortedLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoSortedLists(l1, l2.next)
            return l2

    def partitionAndMerge(
        self, start: int, end: int, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        if start > end:
            return None
        if start == end:
            return lists[start]
        mid = start + (end - start) // 2
        L1 = self.partitionAndMerge(start, mid, lists)
        L2 = self.partitionAndMerge(mid + 1, end, lists)
        return self.mergeTwoSortedLists(L1, L2)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        return self.partitionAndMerge(0, k - 1, lists)
