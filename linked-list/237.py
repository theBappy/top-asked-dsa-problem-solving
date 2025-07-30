# Tc = O(1)
# Sc = O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteNode(node):
    if node is None or node.next is None:
        return
    
    # Copy the next node's value to current node
    node.val = node.next.val
    
    # Save the next node's next pointer
    temp = node.next.next
    
    # Delete the next node
    node.next = temp

