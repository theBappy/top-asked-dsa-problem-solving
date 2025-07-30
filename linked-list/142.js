// Tc = O(n)
// Sc = O(1)
// Floyd cycle detection algorithm
var detectCycle = function(head) {
    if (!head || !head.next) {
        return null;
    }

    let slow = head;
    let fast = head;

    // Phase 1: Detect Cycle
    while (fast !== null && fast.next !== null) {
        slow = slow.next;
        fast = fast.next.next;

        if (slow === fast) {
            break; // Cycle detected
        }
    }

    // If no cycle was found (fast reached the end of the list)
    if (slow !== fast) {
        return null;
    }

    // Phase 2: Find Cycle Start
    let p = head;
    while (p !== slow) {
        p = p.next;
        slow = slow.next;
    }

    return p;
};