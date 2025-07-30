# Tc = O(n) [due to traversal of the linked list]
# Sc = O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteMiddle(head):
    if head is None or head.next is None:
        return None  # If the list is empty or has only one node, return None
    prev_slow = None
    slow = head
    fast = head
    # Use the slow and fast pointer technique to find the middle node
    while fast is not None and fast.next is not None:
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next
    # Remove the middle node
    if prev_slow is not None:
        prev_slow.next = slow.next
    return head
