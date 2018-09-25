"""
dp思路, T: O(n^2), S: O(n^2), 总结一下这一类型叫做中心往边缘扩散类型。特别适用于一种情况下的动态规划：每个问题和其周围边缘的子问题相关。转换为子问题的方式是向四周扩散或者向中心缩小。
"""
class Solution(object):
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