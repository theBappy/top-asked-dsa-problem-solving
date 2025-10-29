
var mergeInBetween = function (list1, a, b, list2) {
    let left = null
    let right = list1
    for (let i = 0; i <= b; i++) {
        if (i === a - 1) {
            left = right
        }
        right = right.next
    }
    left.next = list2
    let temp = list2
    while (temp.next) {
        temp = temp.next
    }
    temp.next = right
    return list1
};