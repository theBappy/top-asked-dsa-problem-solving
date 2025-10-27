
var partition = function (head, x) {
    let small = new ListNode(0)
    let large = new ListNode(0)
    let smallP = small
    let largeP = large
    while (head !== null) {
        if (head.val < x) {
            smallP.next = head
            smallP = smallP.next
        } else {
            largeP.next = head
            largeP = largeP.next
        }
        head = head.next
    }
    smallP.next = large.next
    largeP.next = null
    return small.next
};