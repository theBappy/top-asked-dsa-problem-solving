
var removeZeroSumSublists = function (head) {
    let prefixSum = 0
    const mp = new Map()
    const dummy = new ListNode(0)
    dummy.next = head
    mp.set(0, dummy)

    while (head !== null) {
        prefixSum += head.val

        if (mp.has(prefixSum)) {
            let P = mp.get(prefixSum)
            let start = P
            let pSum = prefixSum
            while (start !== head) {
                start = start.next
                pSum += start.val
                if (start !== head) {
                    mp.delete(pSum)
                }
            }
            P.next = start.next
        } else {
            mp.set(prefixSum, head)
        }
        head = head.next
    }
    return dummy.next
};