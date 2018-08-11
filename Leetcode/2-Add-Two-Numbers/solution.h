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

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// how to get Leetcode tests to run approximately 10-40% faster, since they do a
// lot of print outs.
static auto x = []() {
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    cin.tie(NULL);
    return 0;
}();

class Solution
{
  public:
    /**
     * 63 ms.
     */
    ListNode *addTwoNumbers_v1(ListNode *l1, ListNode *l2)
    {
        ListNode dummy(0), *tail = &dummy; // important line, init a dummy node, and a tail pointer.
        int curry = 0, sum = 0;
        while ((l1 != NULL) && (l2 != NULL))
        {
            sum = l1->val + l2->val + curry;
            if (sum > 9)
            {
                sum = sum % 10;
                curry = 1;
            }
            else
            {
                curry = 0;
            }
            ListNode *new_node = new ListNode(sum);
            tail->next = new_node;
            tail = new_node;
            l1 = l1->next;
            l2 = l2->next;
        }
        if (l1 == NULL)
        {
            // l1 reaches the end.
            while (l2 != NULL)
            {
                sum = l2->val + curry;
                if (sum > 9)
                {
                    sum = sum % 10;
                    curry = 1;
                }
                else
                {
                    curry = 0;
                }
                ListNode *new_node = new ListNode(sum);
                tail->next = new_node;
                tail = new_node;
                l2 = l2->next;
            }
        }
        else if (l2 == NULL)
        {
            while (l1 != NULL)
            {
                sum = l1->val + curry;
                if (sum > 9)
                {
                    sum = sum % 10;
                    curry = 1;
                }
                else
                {
                    curry = 0;
                }
                ListNode *new_node = new ListNode(sum);
                tail->next = new_node;
                tail = new_node;
                l1 = l1->next;
            }
        }
        if (curry == 1)
        {
            ListNode *new_node = new ListNode(1);
            tail->next = new_node;
            tail = new_node;
            tail->next = NULL;
        }
        else
        {
            tail->next = NULL;
        }

        return dummy.next;
    }

    /**
     * 41 ms. 98.55%
     */
    ListNode *addTwoNumbers_v2(ListNode *l1, ListNode *l2)
    {
        ListNode *dummy = new ListNode(0), *current = dummy;
        int sum = 0;
        while (l1 || l2 || sum)
        {
            int l1_val = l1 ? l1->val : 0;
            int l2_val = l2 ? l2->val : 0;
            sum += l1_val + l2_val;
            ListNode *new_node = new ListNode(sum % 10);
            current->next = new_node;
            current = new_node;
            sum /= 10;
            l1 = l1 ? l1->next: NULL; 
            l2 = l2 ? l2->next: NULL;
        }
        return dummy->next;
    }
};
