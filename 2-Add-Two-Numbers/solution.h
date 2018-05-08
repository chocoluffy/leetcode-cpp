using namespace std;

/**

Question:

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4) Output: 7 -> 0 -> 8 Explanation: 342 + 465
= 807.

 */

#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>


struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode *res = NULL;
    int curry = 0, sum = 0;
    while((l1 != NULL) && (l2 != NULL)) {
        sum = l1->val + l2->val + curry;
        if (sum > 9) {
            sum = sum % 10;
            curry = 1;
        } else {
            curry = 0;
        }
        ListNode *new_node = new ListNode(sum);
        new_node->next = res;
        res = new_node;
    }
    if (l1 == NULL) {
        // l1 reaches the end.
        while(l2 != NULL) {
            ListNode *new_node = new ListNode(l2->val);
            new_node->next = res;
            res = new_node;
            l2 = l2->next;
        }
    }
    else if (l2 == NULL) {
        while(l1 != NULL) {
            ListNode *new_node = new ListNode(l1->val);
            new_node->next = res;   
            res = new_node;  
            l1 = l1->next;
        }
    }
    return res;
}

