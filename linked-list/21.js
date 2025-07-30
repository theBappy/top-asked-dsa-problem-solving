
//  Tc = O(n+m) [length of two lists]
//  Sc = (n+m) [due to recursion stack]
class ListNode {
    constructor(val = 0, next = null){
        this.val = val
        this.next = next
    }
}
class Solution{
    mergeTwoLists(list1, list2){
        if(list1 === null){
            return list2
        }
        if(list2 === null){
            return list1
        }
        let result;
        if(list1.val < list2.val){
            result = list1
            result.next = this.mergeTwoLists(list1.next, list2)
        }else{
            result = list2
            result.next = this.mergeTwoLists(list1, list2.next)
        }
        return result
    }
}