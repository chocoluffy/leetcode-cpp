#include <iostream>
#include "solution.h"

int main() {
    Solution s;
    // int result = s.myAtoi("  -2341");
    // int result = s.myAtoi("  -2147483648");
    int result = s.myAtoi("2147483646");
    cout << result << endl;
    // INT_MAX: 2147483647
    return 0;
}
