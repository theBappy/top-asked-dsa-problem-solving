
var modifiedList = function (nums, head) {
    const st = new Set(nums)
    let prev = null
    let curr = head
    while (curr !== null && st.has(curr.val)) {
        head = curr.next
        curr = head
    }
    while (curr != null) {
        const currVal = curr.val
        if (!st.has(currVal)) {
            prev = curr
            curr = curr.next
        } else {
            prev.next = curr.next
            curr = curr.next
        }
    }
    return head
};