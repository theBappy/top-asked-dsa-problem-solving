var swapNodes = function (head, k) {
    const FindLength = (node) => {
        let l = 0;
        let current = node;
        while (current) {
            current = current.next;
            l++;
        }
        return l;
    };
    
    const Length = FindLength(head);

    let k_1 = k;
    let temp1 = head;
    while (k_1 > 1) {
        temp1 = temp1.next;
        k_1--;
    }

    let k_2 = Length - k + 1;
    let temp2 = head;
    while (k_2 > 1) {
        temp2 = temp2.next;
        k_2--;
    }


    const tempVal = temp1.val;
    temp1.val = temp2.val;
    temp2.val = tempVal;

    return head;
};




var swapNodes = function (head, k) {
    let p1 = null
    let p2 = null
    let temp = head
    while (temp !== null) {
        if (p2 !== null) {
            p2 = p2.next
        }
        k--
        if (k === 0) {
            p1 = temp
            p2 = head
        }
        temp = temp.next
    }
    let tempVal = p1.val
    p1.val = p2.val
    p2.val = tempVal
    return head
};