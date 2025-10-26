
var addTwoNumbers = function (l1, l2) {
    const reverseLL = (head) => {
        if (!head || !head.next) {
            return head
        }
        const last = reverseLL(head.next)
        head.next.next = head
        head.next = null
        return last
    }
    l1 = reverseLL(l1)
    l2 = reverseLL(l2)
    let sum = 0
    let carry = 0
    let ans = new ListNode()
    while (l1 || l2) {
        if (l1) {
            sum += l1.val
            l1 = l1.next
        }
        if (l2) {
            sum += l2.val
            l2 = l2.next
        }
        ans.val = sum % 10
        carry = Math.floor(sum / 10)
        const newNode = new ListNode(carry)
        newNode.next = ans
        ans = newNode
        sum = carry
    }
    return carry === 0 ? ans.next : ans
};




var addTwoNumbers = function (l1, l2) {
    const s1 = []
    const s2 = []
    while (l1) {
        s1.push(l1.val)
        l1 = l1.next
    }
    while (l2) {
        s2.push(l2.val)
        l2 = l2.next
    }
    let sum = 0
    let carry = 0
    let ans = new ListNode()
    while (s1.length > 0 || s2.length > 0) {
        if (s1.length > 0) {
            sum += s1.pop()
        }
        if (s2.length > 0) {
            sum += s2.pop()
        }
        ans.val = sum % 10
        carry = Math.floor(sum / 10)
        const newNode = new ListNode(carry)
        newNode.next = ans
        ans = newNode
        sum = carry
    }
    return carry === 0 ? ans.next : ans
};