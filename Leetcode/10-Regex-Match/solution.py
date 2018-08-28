import pprint

# test cases: s = 'aaa', p = 'a*a'

"""
challenges:
- given a dynamic programming occurrence rules, don't know how to convert into
  code, espeically about how to iterate.


mine:
- bottom up method. 

"""


class Solution(object):

    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        pprint.pprint(dp)
        return dp[0][0]

    # error. fail at the case: print Solution().isMatch('aa', 'aaa')
    def isMatch_v1(self, s, p):
        """
        :type s: str :type p: str :rtype: bool
        """
        pad = max(len(s) + 1, len(p) + 1)
        dp = [[False] * pad for _ in range(pad)]
        print len(dp)
        for i in range(len(dp[0])):
            dp[0][i] = True
        for i in range(len(s)):
            for j in range(i, len(p)):
                if s[i] == p[j] or p[j] == '.':
                    dp[i+1][j+1] = dp[i][j]
                elif s[i] != p[j] and p[j] != '*':
                    dp[i+1][j+1] = False
                elif s[i] != p[j] and p[j] == '*':
                    dp[i+1][j+1] = dp[i-1][j-1] or dp[i+1][j]
        pprint.pprint(dp)
        return dp[len(s)][len(p)]

# print Solution().isMatch('aaba', 'a.ba*') print Solution().isMatch('ab', '.*')
print Solution().isMatch('aa', 'aaa')
