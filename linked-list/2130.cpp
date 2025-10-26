// Using vectors
class Solution {
public:
    int pairSum(ListNode* head) {
        vector<int> vec;
        ListNode* curr = head;
        while (curr != NULL) {
            vec.push_back(curr->val);
            curr = curr->next;
        }
        int result = 0;
        int i = 0;
        int j = vec.size() - 1;
        while (i < j) {
            result = max(result, vec[i] + vec[j]);
            i++;
            j--;
        }
        return result;
    }
};

// Using stack
