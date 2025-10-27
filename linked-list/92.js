
var reverseBetween = function (head, left, right) {
    if (head === null || head.next === null) {
        return head
    }
    let dummy = new ListNode(0)
    dummy.next = head
    let prev = dummy
    for (let i = 1; i < left; i++) {
        prev = prev.next
    }
    let curr = prev.next
    for (let i = 1; i <= right - left; i++) {
        let temp = prev.next
        prev.next = curr.next
        curr.next = curr.next.next
        prev.next.next = temp
    }
    return dummy.next
};