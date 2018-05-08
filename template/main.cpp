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

int main() {
    Solution s;
    return 0;
}
