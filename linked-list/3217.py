class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        st = set(nums)
        prev = None
        curr = head
        while curr is not None and curr.val in st:
            head = curr.next
            curr = head
        while curr is not None:
            currVal = curr.val
            if currVal not in st:
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next
        return head
