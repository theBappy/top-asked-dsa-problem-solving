class ListNode {
    constructor(val = 0, next = null){
        this.val = val
        this.next = next
    }
}
function deleteMiddle(head){
    if(head === null || head.next === null) return null
    let prevSlow = null
    let slow = head
    let fast = head
    while(fast && fast.next){
        prevSlow = slow
        slow = slow.next
        fast = fast.next.next
    }
    if(prevSlow){
        prevSlow.next = slow.next
    }
    return head
}