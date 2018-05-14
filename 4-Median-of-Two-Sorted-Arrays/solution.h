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

static auto x = []() {
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    cin.tie(NULL);
    return 0;
}();

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            // ensure nums1.size always smaller than nums2.
            vector<int>& tmp = nums1;
            nums1 = nums2;
            nums2 = tmp;
        }
        int s1_size = nums1.size(), s2_size = nums2.size();
        int if_odd = (s1_size + s2_size) % 2;
        int target_len = (s1_size + s2_size) / 2;
        target_len = if_odd == 0 ? target_len : target_len - 1;
        int s1_min = 0; // min element index.
        int s1_max = s1_size - 1;
        int s1_cut, s2_cut;
        int l_max, r_min, lmax_in_s1;
        while (s1_min <= s1_max) {
            s1_cut = (int)((s1_min + s1_max)/2);
            s2_cut = target_len - (s1_cut + 1) - 1;
            if (nums1[s1_cut] > nums2[s2_cut]) {
                l_max = nums1[s1_cut];
                lmax_in_s1 = 1;
            } else {
                l_max = nums2[s2_cut];
                lmax_in_s1 = 0;
            }
            r_min = nums1[s1_cut + 1] < nums2[s2_cut + 1] ? nums1[s1_cut + 1] : nums2[s2_cut + 1];
            if (l_max <= r_min) {
                return if_odd == 0 ? (double)((l_max + r_min)/2) : r_min;
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
        return if_odd == 0 ? (double)((l_max + r_min)/2) : r_min;
    }
};
