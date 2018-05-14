#include <iostream>
#include "solution.h"

int main() {
    Solution s;
    int num1[] = {3, 4};
    int num2[] = {1, 2};
    vector<int> s1 (num1, num1 + sizeof(num1) / sizeof(int) );
    vector<int> s2 (num2, num2 + sizeof(num2) / sizeof(int) );
    double test1 = s.findMedianSortedArrays(s1, s2);
    cout << test1 << endl;
    return 0;
}
