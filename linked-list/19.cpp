
// 2 Pass Solution

class Solution {
public:
    int getLength(ListNode* head){
        int len = 0;
        while(head){
            len++;
            head = head->next;
        }
        return len;
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int l = getLength(head);
        if (l == n) {
            ListNode* temp = head->next;
            delete (head);
            return temp;
        }
        int travel = l - n;
        ListNode* temp = head;
        ListNode* prev = NULL;
        while (travel--) {
            prev = temp;
            temp = temp->next;
        }
        prev->next = temp->next;
        delete (temp);
        return head;
    }
};

// One Pass

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* temp = head;
        for (int i = 1; i <= n; i++) {
            temp = temp->next;
        }
        if (temp == NULL) {
            ListNode* result = head->next;
            delete (head);
            return result;
        }
        ListNode* prev = head;
        while (temp != NULL && temp->next != NULL) {
            prev = prev->next;
            temp = temp->next;
        }
        ListNode* deleteNode = prev->next;
        prev->next = prev->next->next;
        delete(deleteNode);
        return head;
    }
};