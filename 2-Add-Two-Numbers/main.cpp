#include <iostream>
#include "solution.h"

// how to get Leetcode tests to run approximately 10-40% faster, since they do a
// lot of print outs.
static auto x = [](){
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    cin.tie(NULL);
    return 0;
}();

ListNode *create_linkedlist(std::initializer_list<int> lst)
{
    auto iter = lst.begin();
    ListNode *head = lst.size() ? new ListNode(*iter++) : NULL;
    for (ListNode *cur=head; iter != lst.end(); cur=cur->next)
        cur->next = new ListNode(*iter++);
    return head;
}

int main()
{
    Solution s;
    ListNode *l1 = create_linkedlist({2,4,3});
    ListNode *l2 = create_linkedlist({5,6,4});
    ListNode *ret = s.addTwoNumbers(l1, l2);
    for (ListNode *cur = ret; cur; cur = cur->next)
        cout << cur->val << "->";
    cout << "\b\b  " << endl;

    return 0;
}

