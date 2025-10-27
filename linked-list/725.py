#  Amazon, Google
# T.C : O(L+k) - traversing the input linkedlist only once and the array of size k only once
# S.C : O(1) (Not including result vector)


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr  = head
        l = 0
        while curr:
            l += 1
            curr = curr.next
        minContain = l // k
        remainder = l % k
        result = [None] * k
        curr = head
        prev = None
        for i in range(k):
            result[i] = curr
            for count in range(1, minContain + (1 if remainder > 0 else 0) + 1):
                prev = curr
                if curr:
                    curr = curr.next
            if prev:
                prev.next = None
            remainder -= 1
        return result

        