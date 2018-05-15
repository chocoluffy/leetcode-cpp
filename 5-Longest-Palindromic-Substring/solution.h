using namespace std;

/**

Question:

Given a string s, find the longest palindromic substring in s. You may assume
that the maximum length of s is 1000.

Example 1:

Input: "babad" Output: "bab" Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd" Output: "bb"

 */

#include <algorithm> // use reverse()

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
     * 162 ms. 22%.
     */
    string longestPalindrome(string s) {
        string s_reverse = s;
        reverse(s_reverse.begin(), s_reverse.end());
        int s_size = s.size();
        int LCSuffix[s_size + 1][s_size + 1]; // finding longest common suffix using dynamic programming.
        int lcsubstring_len = 0, mark_position = 0;
        for (int i = 0; i <= s_size; i++) {
            for (int j = 0; j <= s_size; j++) {
                if (i == 0 || j == 0) {
                    LCSuffix[i][j] = 0;
                }
                else if (s[i-1] == s_reverse[j-1]) {
                    LCSuffix[i][j] = LCSuffix[i-1][j-1] + 1;
                    if (LCSuffix[i][j] > lcsubstring_len && (i + j == s_size + LCSuffix[i][j])) {
                        /**
                         * i + j == s_size + LCSuffix[i][j]
                         * this condition ensure that palindrome is continuous substring rather than subsequence.
                         */
                        lcsubstring_len = LCSuffix[i][j];
                        mark_position = i;
                    }
                } else {
                    LCSuffix[i][j] = 0;
                }
            }
        }
        string result = s.substr(mark_position - lcsubstring_len, lcsubstring_len);
        return result;
    }
};