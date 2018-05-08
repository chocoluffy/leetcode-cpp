#include <iostream>
#include "solution.h"

/**
 * 6ms. 
 */
// how to get Leetcode tests to run approximately 10-40% faster, since they do a lot of print outs.
static auto x = [](){
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    cin.tie(NULL);
    return 0;
}();

int main() {
    vector<int> input = {1, 2, 3, 8, 4, 9};
    int target = 10;
    vector<int> result = twoSum_v2(input, target);
    cout << result[0] << " " << result[1];
    return 0;
}
