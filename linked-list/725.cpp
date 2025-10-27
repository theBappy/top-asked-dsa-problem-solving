// Amazon, Google
//T.C : O(L+k) - traversing the input linkedlist only once and the array of size k only once
//S.C : O(1) (Not including result vector)

class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        ListNode* curr = head;
        int l = 0;
        while (curr) {
            l++;
            curr = curr->next;
        }
        int minCotain = l / k;
        int remainder = l % k;
        vector<ListNode*> result(k, NULL);
        curr = head;
        ListNode* prev = NULL;
        for (int i = 0; i < k; i++) {
            result[i] = curr;
            for (int count = 1; count <= minCotain + (remainder > 0 ? 1 : 0);
                 count++) {
                prev = curr;
                curr = curr->next;
            }
            if (prev != NULL) {
                prev->next = NULL;
            }
            remainder--;
        }
        return result;
    }
};