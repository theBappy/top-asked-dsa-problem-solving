
var removeNthFromEnd = function (head, n) {
    let temp = head
    for (let i = 1; i <= n; i++) {
        temp = temp.next
    }
    if (temp === null) {
        let result = head.next
        return result
    }
    let prev = head
    while (temp && temp.next) {
        prev = prev.next
        temp = temp.next
    }
    prev.next = prev.next.next
    return head
};