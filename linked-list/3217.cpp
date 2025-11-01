//Approach (Using Simple straight forward approach)
//T.C : O(n)
//S.C : O(n)
class Solution {
public:
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        unordered_set<int> st(begin(nums), end(nums));
        ListNode* prev = NULL;
        ListNode* curr = head;


        while (curr != NULL && st.count(curr->val)) {
            head = curr->next;
            curr = head;
        }

        while (curr != NULL) {
            int currVal = curr->val;
            if (!st.count(currVal)) {
                prev = curr;
                curr = curr->next;
            } else {
                prev->next = curr->next;
                curr = curr->next;
            }
        }
        return head;
    }
};