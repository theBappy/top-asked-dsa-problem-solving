// Tc = O(n)
// Sc = O(1)
// Hair & Tortoise technique

class Solution {
    middleNode(head){
        let slow = head
        let fast = head
        while(fast !== null && fast.next !== null){
            slow = slow.next
            fast = fast.next.next
        }
        return slow
    }
}