"""
Given a triangle, find the minimum path sum from top to bottom. Each step you
may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7], [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is
the total number of rows in the triangle.
"""

class Solution(object):
    # T: O(n^2), S: O(n^2)
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]] :rtype: int
        """
        n = len(triangle)
        m = len(triangle[-1])
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(0, m-(n-1-i)):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        return dp[0][0]
        
    # Space complexity can be improved to linear, since the subproblems only
    # depends on the prev level.
    def minimumTotal_v2(self, triangle):
        n = len(triangle)
        m = len(triangle[-1])
        dp = [0] * (m+1)
        for i in range(n-1, -1, -1):
            for j in range(0, m-(n-1-i)):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]
        
    