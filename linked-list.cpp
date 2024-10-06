/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
    // Handle edge case of empty list or single node
        if (!head || !head->next) return head;
        
        ListNode dummy(0, head);
        ListNode* prev = &dummy;
        
        while (head && head->next) {
            if (head->val == head->next->val) {
                // Skip nodes with duplicate values
                while (head->next && head->val == head->next->val) {
                    head = head->next;
                }
                // Connect prev to the next distinct node
                prev->next = head->next;
            } else {
                prev = prev->next;
            }
            head = head->next;
        }
        
        return dummy.next;
    }
};
