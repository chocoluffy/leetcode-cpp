using namespace std;

/**

Question:

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should
be O(log (m+n)).

Example 1: nums1 = [1, 3] nums2 = [2]

The median is 2.0

Example 2: nums1 = [1, 2] nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

 */

#include <vector>
#include <math.h>

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
     * 42 ms. 98%.
     */
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            // ensure nums1.size always smaller than nums2.
            nums1.swap(nums2);
        }
        int s1_size = nums1.size(), s2_size = nums2.size();
        int if_odd = (s1_size + s2_size) % 2;
        int target_len = (s1_size + s2_size) / 2;
        if (s1_size == 0) {
            // edge case: nums1 is empty.
            return if_odd == 0 ? (double)(((double)nums2[s2_size/2 - 1] + (double)nums2[s2_size/2])/2) : nums2[s2_size/2];    
        }
        int s1_min = -1; // min element index.
        int s1_max = s1_size - 1;
        int s1_cut, s2_cut;
        int l_max, r_min, lmax_in_s1;
        while (s1_min <= s1_max) {
            s1_cut = floor((((double)s1_min + (double)s1_max)/2));
            s2_cut = target_len - (s1_cut + 1) - 1;
            if (s2_cut < 0) {
                // edge case: nums1 takes exactly half element.
                return if_odd == 0 ? (double)(((double)nums1[s1_cut] + (double)nums2[0])/2) : (double)nums2[0];
            }
            if (nums1[s1_cut] > nums2[s2_cut] && s1_cut >= 0) {
                // edge case: when s1_cut == -1, continue.
                l_max = nums1[s1_cut];
                lmax_in_s1 = 1;
            } else {
                l_max = nums2[s2_cut];
                lmax_in_s1 = 0;
            }
            if (s1_cut + 1 == s1_size) {
                // num1 cannot contribute to right hand side.
                r_min = nums2[min(s2_cut + 1, s2_size)];
            } else if (s2_cut + 1 == s2_size) {
                // num2 cannot contribute to the right hand side.
                r_min = nums1[min(s1_cut + 1, s1_size)];
            } else {
                r_min = nums1[min(s1_cut + 1, s1_size)] < nums2[min(s2_cut + 1, s2_size)] ? nums1[min(s1_cut + 1, s1_size)] : nums2[min(s2_cut + 1, s2_size)];
            }
            if (l_max <= r_min) {
                return if_odd == 0 ? (double)(((double)l_max + (double)r_min)/2) : (double)r_min;
            } else {
                // need to adjust the cut position in s1;
                if (lmax_in_s1) {
                    // s1_cut moves left.
                    s1_max = s1_cut - 1;
                } else {
                    // s1_cut moves right.
                    s1_min = s1_cut + 1;
                }
            }
        }
        return if_odd == 0 ? (double)(((double)l_max + (double)r_min)/2) : (double)r_min;
    }
};
