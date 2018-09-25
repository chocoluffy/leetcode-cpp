import pprint
"""
Typical question convert:
- finding longest common suffix in all prefix pairs of two string.
=> "all prefix pairs" equals to a dp table, where dp[i][j] represent the prefix pair of s1[:i+1] and s2[:j+1]
=> given such dp table, to find the longest common suffix:
   constantly aligning with last elements and increment, till not match.
   LCSuffix[i][j] = LCSuffic[i-1][j-1] + 1 if s1[i] == s2[j]
"""


class Solution(object):
    def longest_common_substring(self, s1, s2):
        table = [[0] * (len(s1)+1) for _ in range(len(s2) + 1)]
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    table[i][j] = table[i-1][j-1] + 1
                else:
                    table[i][j] = 0
        pprint.pprint(table)
        max_len = 0
        for i in range(len(table)):
            for j in range(len(table[0])):
                if table[i][j] > max_len:
                    max_len = table[i][j]
                    target_index = j
        return s2[target_index - max_len:target_index]

    # use dp.
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        max_len = 1
        start_index = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        # a single char is a valid palindrome.
        for i in range(n):
            for j in range(n):
                if i == j:
                    dp[i][i] = True
        for window in range(1, n):
            for i in range(0, n - window):
                right = i + window
                if window == 1:  # for case to two chars.
                    if s[i] == s[right]:
                        dp[i][right] = True
                        max_len = max(max_len, window + 1)
                        start_index = i
                else:
                    if dp[i + 1][right - 1] and s[i] == s[right]:
                        dp[i][right] = True
                        max_len = max(max_len, window + 1)
                        start_index = i
        return s[start_index: start_index + max_len]


print Solution().longest_palindrome('babad')
# print Solution().longest_common_substring('abcccc', 'ccccab')
