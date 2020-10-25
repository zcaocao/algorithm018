/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/* Iteration */
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2){
    if (l1 == NULL) return l2;
    if (l2 == NULL) return l1;
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* prev;
    prev = dummy;
    while ((l1 != NULL) && (l2 != NULL)) {
        if (l1->val < l2->val) {
            prev->next = l1;
            l1 = l1->next;
        }
        else {
            prev->next = l2;
            l2 = l2->next;
        } 
        prev = prev->next;
    } 
    prev->next = (l1 == NULL) ? l2 : l1;
    return dummy->next;
}
