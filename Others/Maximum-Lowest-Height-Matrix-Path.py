# -*- coding: utf-8 -*-
"""
Amazon OA2:
2. 给一个二维矩阵，表示某点的高度，人从左上角出发， 只能向下或向右走，最终到达右下角。
求所有可能的路径中每个路径最低点的最大值。
典型DP， 类似LC174
"""

import pprint
class Solution():
    def max_min_height(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        for j in range(m):
            dp[0][j] = matrix[0][j]
        for i in range(n):
            dp[i][0] = matrix[i][0]

        for i in range(1, n):
            for j in range(1, m):
                prev = max(dp[i-1][j], dp[i][j-1])
                if matrix[i][j] < prev:
                    dp[i][j] = matrix[i][j]
                else:
                    dp[i][j] = prev
        # pprint.pprint(dp)
        return dp[n-1][m-1]

print Solution().max_min_height([
    [8, 2, 7, 8], 
    [7, 8, 4, 5],
    [1, 8, 2, 2],
    [1, 6, 6, 6]
    ])