
var swapPairs = function(head) {
    if(head === null || head.next === null){
        return head
    }
    let temp = head.next
    head.next = swapPairs(head.next.next)
    temp.next = head
    return temp
};