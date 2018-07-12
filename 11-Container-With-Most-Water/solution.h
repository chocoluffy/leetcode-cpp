using namespace std;

/**

Question:

Given n non-negative integers a1, a2, ..., an, where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 */

#include <vector>
#include <algorithm>

static auto x = []() {
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    cin.tie(NULL);
    return 0;
}();

class Solution {
public:
    /**
     * 4 ms, 100%.
     */
    int maxArea(vector<int>& height) {
        int i = 0, j = height.size() - 1;
        int maxarea = 0;
        while(i < j) {
            maxarea = max(maxarea, min(height[i], height[j]) * (j - i));
            if (height[i] < height[j]) {
                i++;
            } else if (height[i] > height[j]) {
                j--;
            } else {
                i++; j--;
            }
        }
        return maxarea;
    }
};