# Tc = O(n)
# Sc = O(1)
# Floyd's Cycle-Finding Algorithm
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        slow = head
        fast = head

        # Phase 1: Detect Cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break # Cycle detected

        # If no cycle was found (fast reached the end of the list)
        if slow != fast:
            return None

        # Phase 2: Find Cycle Start
        p = head
        while p != slow:
            p = p.next
            slow = slow.next

        return p

