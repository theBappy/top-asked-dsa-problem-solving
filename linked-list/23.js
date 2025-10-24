var mergeKLists = function (lists) {
    const mergeTwoSortedLists = (l1, l2) => {
        if (!l1) return l2
        if (!l2) return l1
        if (l1.val <= l2.val) {
            l1.next = mergeTwoSortedLists(l1.next, l2)
            return l1
        } else {
            l2.next = mergeTwoSortedLists(l1, l2.next)
            return l2
        }
    }
    const partitionAndMerge = (start, end) => {
        if (start > end) return null
        if (start === end) return lists[start]
        const mid = start + Math.floor((end - start) / 2)
        const L1 = partitionAndMerge(start, mid)
        const L2 = partitionAndMerge(mid + 1, end)
        return mergeTwoSortedLists(L1, L2)
    }
    const k = lists.length
    if (k === 0) return null
    return partitionAndMerge(0, k - 1)
};