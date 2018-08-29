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

    def isMatch_official(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                print i, j
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

    # recursion version
    def isMatch_mine(self, s, p):
        # when there is no '*'
        if len(s) > 0 and len(p) == 0:
            return False
        elif len(s) == 0 and len(p) == 0:
            return True
        first_match = len(s) > 0 and (s[0] == p[0] or p[0] == '.')

        if len(p) > 1 and p[1] == '*':
            return self.isMatch_mine(s, p[2:]) or (first_match and self.isMatch_mine(s[1:], p))
        else:
            if first_match:
                return self.isMatch_mine(s[1:], p[1:])
            else:
                return False

    # dp version
    def isMatch(self, s, p):
        table = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        table[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
                if j+1 < len(p) and p[j+1] == '*':
                    table[i][j] = (first_match and table[i+1][j]
                                   ) or table[i][j+2]
                else:
                    table[i][j] = first_match and table[i+1][j+1]
        pprint.pprint(table)
        return table[0][0]


# print Solution().isMatch('aaba', 'a.ba*') 
# print Solution().isMatch('ab', '.*')
# print Solution().isMatch('aa', 'aaa')

print Solution().isMatch('mississippi', 'mis*is*p*.')
