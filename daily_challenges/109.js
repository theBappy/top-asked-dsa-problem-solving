/*
Time complexity: O(n log(n)).
There are log(n) recursive levels because each time we split it to half, and in each level we loop through the whole list, divided into small parts.
Space complexity: O(log(n)).
We don't consider the returning tree as extra space, but we have log(n) recursive calls on stack.
*/


var sortedListToBST = function (head) {
    if (!head) {
        return null;
    }
    if (!head.next) {
        return new TreeNode(head.val);
    }

    let slow = head;
    let fast = head;
    let slow_prev = head;

    while (fast && fast.next) {
        slow_prev = slow;
        slow = slow.next;
        fast = fast.next.next;
    }

    const root = new TreeNode(slow.val);

    slow_prev.next = null;
    root.left = sortedListToBST(head);
    root.right = sortedListToBST(slow.next);

    return root;
};