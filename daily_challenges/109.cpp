/*
Time complexity: O(n log(n)).
There are log(n) recursive levels because each time we split it to half, and in each level we loop through the whole list, divided into small parts.
Space complexity: O(log(n)).
We don't consider the returning tree as extra space, but we have log(n) recursive calls on stack.
*/


class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        if (!head) {
            return NULL;
        }
        if (!head->next) {
            return new TreeNode(head->val);
        }
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* slow_prev = head;
        while (fast && fast->next) {
            slow_prev = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        TreeNode* root = new TreeNode(slow->val);
        
        slow_prev->next = NULL;
        root->left = sortedListToBST(head);
        root->right = sortedListToBST(slow->next);

        return root;
    }
};