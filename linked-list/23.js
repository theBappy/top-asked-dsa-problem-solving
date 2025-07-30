

// Definition for singly-linked list.
class ListNode {
    constructor(val = 0, next = null) {
        this.val = val; // The value of the current node
        this.next = next; // Pointer to the next node in the list
    }
}

class Solution {
    mergeTwoSortedLists(l1, l2) {
        // Base case: if the first list is empty, return the second list.
        if (l1 === null) return l2;
        // Base case: if the second list is empty, return the first list.
        if (l2 === null) return l1;

        // Compare the values of the current nodes from both lists.
        if (l1.val < l2.val) {
            // If l1's value is smaller, it becomes the head of the merged list.
            // Recursively merge the rest of l1 (l1.next) with l2,
            // and set the result as the next node of l1.
            l1.next = this.mergeTwoSortedLists(l1.next, l2);
            // Return l1 as the head of the merged list.
            return l1;
        } else {
            // If l2's value is smaller or equal, it becomes the head of the merged list.
            // Recursively merge l1 with the rest of l2 (l2.next),
            // and set the result as the next node of l2.
            l2.next = this.mergeTwoSortedLists(l1, l2.next);
            // Return l2 as the head of the merged list.
            return l2;
        }
    }
    partitionAndMerge(start, end, lists) {
        // Base case 1: If the start and end indices are the same,
        // it means we have reached a single list. Return that list.
        // This was the correction needed. The original returned `null` here.
        if (start === end) {
            return lists[start];
        }
        // Base case 2: If the start index is greater than the end index,
        // it means the range is invalid or empty. Return null.
        if (start > end) {
            return null;
        }

        // Calculate the middle index to divide the array of lists.
        // Using Math.floor for integer division.
        const mid = start + Math.floor((end - start) / 2);

        // Recursively merge the left half of the lists.
        const l1 = this.partitionAndMerge(start, mid, lists);
        // Recursively merge the right half of the lists.
        const l2 = this.partitionAndMerge(mid + 1, end, lists);

        // Merge the two sorted lists obtained from the left and right halves.
        return this.mergeTwoSortedLists(l1, l2);
    }

    /**
     * Merges k sorted linked lists into one single sorted linked list.
     * @param {ListNode[]} lists An array of ListNode heads representing k sorted linked lists.
     * @returns {ListNode} The head of the merged sorted linked list, or null if no lists are provided.
     */
    mergeKLists(lists) {
        const k = lists.length; // Get the number of linked lists.

        // If there are no lists, return null.
        if (k === 0) {
            return null;
        }

        // Initiate the divide-and-conquer process starting with all lists.
        // The result will be the head of the final merged linked list.
        return this.partitionAndMerge(0, k - 1, lists);
    }
}