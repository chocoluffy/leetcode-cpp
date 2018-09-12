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
        if s1[i-1] == s2[j-1]: # always pay attention that the i, j here is for table, when refer in string, use i-1, j-1
          table[i][j] = table[i-1][j-1] + 1
        else:
          table[i][j] = 0
    pprint.pprint(table)
    max_len = 0
    for i in range(len(table)):
        for j in range(len(table[0])):
            max_len = table[i][j] if table[i][j] > max_len else max_len
    return max_len

print Solution().longest_common_substring('abcccc', 'ccccab')


