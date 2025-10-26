# reverse function take O(n) and O(n) for a list of length n, due to visiting each node once with recursion
# reverse both l1 and l2 takes O(n) where n is the length of the longer list
# while loop run O(max(m, n))
# Total Tc = O(m + n)
# Total Sc = O(m + n)

class Solution:
    def reverseLL(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        last = self.reverseLL(head.next)
        head.next.next = head
        head.next = None
        return last

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverseLL(l1)
        l2 = self.reverseLL(l2)
        sum_ = 0
        carry = 0
        ans = ListNode()
        while l1 or l2:
            if l1:
                sum_ += l1.val
                l1 = l1.next
            if l2:
                sum_ += l2.val
                l2 = l2.next
            ans.val = sum_ % 10
            carry = sum_ // 10
            newNode = ListNode(carry)
            newNode.next = ans
            ans = newNode
            sum_ = carry
        return ans.next if carry == 0 else ans


# Using Stack
# Tc = O(n + m), which simplifies to O(max(n, m)) since the dominant factor is the longer list. This is efficient for typical linked list lengths.
# Sc = O(n+m)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        sum_ = 0
        carry = 0
        ans = ListNode()
        while s1 or s2:
            if s1:
                sum_ += s1.pop()
            if s2:
                sum_ += s2.pop()

            ans.val = sum_ % 10
            carry = sum_ // 10

            newNode = ListNode(carry)
            newNode.next = ans
            ans = newNode
            sum_ = carry
        return ans.next if carry == 0 else ans
