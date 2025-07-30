/**
 * // Definition for a _Node.
 * function _Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {_Node} head
 * @return {_Node}
 */
var copyRandomList = function(head) {
     const oldToCopy = new Map()
     oldToCopy.set(null, null)
        
        let curr = head;
        while (curr) {
            const copy = new Node(curr.val);
            oldToCopy.set(curr, copy)
            curr = curr.next;
        }

        curr = head;
        while (curr) {
            const copy = oldToCopy.get(curr)
            copy.next = oldToCopy.get(curr.next)
            copy.random = oldToCopy.get(curr.random)
            curr = curr.next;
        }

        return oldToCopy.get(head);
};