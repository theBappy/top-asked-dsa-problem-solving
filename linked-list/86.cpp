//Tc = O(n)
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode* small = new ListNode(0);
        ListNode* large = new ListNode(0);
        ListNode* smallP = small;
        ListNode* largeP = large;
        while (head != NULL) {
            if (head->val < x) {
                smallP->next = head;
                smallP = smallP->next;
            } else {
                largeP->next = head;
                largeP = largeP->next;
            }
            head = head->next;
        }
        smallP->next = large->next;
        largeP->next = NULL;
        return small->next;
    }
};