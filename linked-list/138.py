# O(n)
# O(n)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        curr = head
        while head:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        return oldToCopy[head]



# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         oldToCopy = {None: None}
#         curr = head
#         while curr:
#             copy = Node(curr.val)
#             oldToCopy[curr] = copy
#             curr.next = next
        
#         curr = head
#         while curr:
#             copy = oldToCopy[curr]
#             copy.next = oldToCopy[curr.next]
#             copy.random = oldToCopy[curr.random]
#             curr = curr.next
#         return oldToCopy[head]