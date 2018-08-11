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

#include <algorithm>  // use reverse()

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
   * - construct string in reverse order, convert the question into finding
   *   longest common substring with some position requirement satisfied.
   */
  string longestPalindrome_v1(string s) {
    string s_reverse = s;
    reverse(s_reverse.begin(), s_reverse.end());
    int s_size = s.size();
    int LCSuffix[s_size + 1][s_size + 1];  // finding longest common suffix
                                           // using dynamic programming.
    int lcsubstring_len = 0, mark_position = 0;
    for (int i = 0; i <= s_size; i++) {
      for (int j = 0; j <= s_size; j++) {
        if (i == 0 || j == 0) {
          LCSuffix[i][j] = 0;
        } else if (s[i - 1] == s_reverse[j - 1]) {
          LCSuffix[i][j] = LCSuffix[i - 1][j - 1] + 1;
          if (LCSuffix[i][j] > lcsubstring_len &&
              (i + j == s_size + LCSuffix[i][j])) {
            /**
             * i + j == s_size + LCSuffix[i][j] this condition ensure that
             * palindrome is continuous substring rather than subsequence.
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

  /**
   * 165 ms. 21%.
   * - same idea, but use pointer move in reverse order rather than copy a new
   *   string.
   */
  string longestPalindrome_v2(string s) {
    int s_size = s.size();
    int LCSuffix[s_size + 1][s_size + 1];  // finding longest common suffix
                                           // using dynamic programming.
    int lcsubstring_len = 0, mark_position = 0;
    for (int i = 0; i <= s_size; i++) {
      for (int j = 0; j <= s_size; j++) {
        int j_reverse = s_size - j;
        if (i == 0 || j == 0) {
          LCSuffix[i][j] = 0;
        } else if (s[i - 1] == s[j_reverse]) {
          LCSuffix[i][j] = LCSuffix[i - 1][j - 1] + 1;
          if (LCSuffix[i][j] > lcsubstring_len &&
              (i + j == s_size + LCSuffix[i][j])) {
            /**
             * i + j == s_size + LCSuffix[i][j] this condition ensure that
             * palindrome is continuous substring rather than subsequence.
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

  /**
   * 15 ms, 78%.
   * - more straightforward idea: for loop each element, and expand from each
   *   one to exmain if it is a palindrome string.
   * - there are two kinds of palindrome pattern: aba and abba, both are valid.
   */
  string longestPalindrome_v3(string s) {
    int max = 1, start = 0;
    for (int i = 0; i < s.size() - 1; i++) {
      int left = i;
      int right = i + 1;
      while (left >= 0 && right <= s.size() - 1 && s[left] == s[right]) {
        left--;
        right++;
      }
      // note now left and right are beyond the valid range.
      if (right - left - 1 > max) {
        max = right - left - 1;
        start = left + 1;
      }

      left = i;
      right = i + 2;
      while (left >= 0 && right <= s.size() - 1 && s[left] == s[right]) {
        left--;
        right++;
      }
      if (right - left - 1 > max) {
        max = right - left - 1;
        start = left + 1;
      }
    }
    cout << start << " " << max << endl;
    return s.substr(start, max);
  }

  /**
   * 4ms. 100%.
   * - compared with above, only expand at right,
   * - trick: view repeated elements as one single elements. because
   *   repeated elements, no matter how long it is, can still be viewed as valid
   *   palindrome. such as: ccbbbbcc, ccbcc.
   */
  string longestPalindrome(string s) {
    int max = 1, start = 0;
    for (int i = 0; i < s.size() - 1; i++) {
      int left = i, right = i;
      while (right < s.size() - 1 && s[right] == s[right + 1]) right++;
      i = right;
      while (left > 0 && right < s.size() - 1 && s[left - 1] == s[right + 1]) {
        left--;
        right++;
      }
      if (right - left + 1 > max) {
        max = right - left + 1;
        start = left;
      }
    }
    return s.substr(start, max);
  }
};