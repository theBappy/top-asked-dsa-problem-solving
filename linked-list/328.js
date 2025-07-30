function(head) {
    if(!head || !head.next){
        return head
    }
    let odd = head
    let even = head.next
    let evenHead = even
    while(even !== null && even.next !== null){
        odd.next = even.next
        odd = odd.next
        even.next = even.next.next
        even = even.next
    }
    odd.next = evenHead
    return head
};