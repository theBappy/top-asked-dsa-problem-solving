class Solution {
    reverseList(head){
        if(head === null || head.next === null){
            return head
        }
        const last = this.reverseList(head.next)
        head.next.next = head
        head.next = null
        return last
    }
}