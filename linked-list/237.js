function(node) {
    if(!node || !node.next) return
    node.val = node.next.val
    node.next = node.next.next
};