"""
Good explanation:
- After a few hours of pondering. I finally figure out this brilliant
DP solution. Here is my understanding about dp[i][k] dp[i][j]: coins obtained
from bursting all the balloons between index i and j (not including i or j)
dp[i][j] = max(nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]) (k in (i+1,j))
If k is the index of the last balloon burst in (i, j), the coins that burst will
get are nums[i] * nums[k] * nums[j], and to calculate dp[i][j], we also need to
add the coins obtained from bursting balloons between i and k, and between k and
j, i.e., dp[i][k] and dp[k][j]

summary:
- think backward. only related to boundary. 
- ballon already bursted has no effect on the remained problem.
- DP[i][j] = max(DP[i][j], A[i]*A[k]*A[j] + DP[i][k] + DP[k][j])
DP[i][j] give max coin earned within i, j boundary. not including i and j.
A[k] is the last baloon to burst within the range
"""
import pprint
class Solution(object):
    # maximum recursion depth reached.
    def maxCoins(self, nums):
        """
        :type nums: List[int] :rtype: int
        """
        res = 0
        padded_nums = [1] + nums + [1]
        for i in xrange(1, len(padded_nums) + 1):
            new_nums = padded_nums[:i] + padded_nums[i+1:]
            res = max(res, self.maxCoins(new_nums) + padded_nums[i-1]*padded_nums[i]*padded_nums[i+1])
        return res
    
    # use divide and conquer, instead of reduce the length one by one, try cut
    # the list by half each time. => same error: maximum recursion depth
    # reached. 
    def maxCoins_v2(self, nums):
        def maxCoins_helper(nums, start, end):
            res = 0
            if start == end:
                curr_left = 1 if start-1 < 0 else nums[start-1]
                curr_right = 1 if start+1 == len(nums) else nums[start+1]
                curr_sum = nums[start] * curr_left * curr_right
            for i in xrange(end - start + 1):
                left_max = maxCoins_helper(nums, start, i)
                right_max = maxCoins_helper(nums, i+1, end)
                curr_left = 1 if i-1 < 0 else nums[i-1]
                curr_right = 1 if i+1 == len(nums) else nums[i+1]
                curr_sum = nums[i] * curr_left * curr_right
                res =  max(res, curr_sum + left_max + right_max)
            return res
        if not nums:
            return 0
        return maxCoins_helper(nums, 0, len(nums)-1)

    def maxCoins_v3(self, nums):
        new_nums = [1] + nums + [1]
        n = len(new_nums)
        DP = [[0] * n for _ in range(n)]
        for k in range(2, n):
            for l in range(0, n-k):
                r = l + k
                for i in range(l+1, r):
                    DP[l][r] = max(DP[l][r], new_nums[l]*new_nums[i]*new_nums[r] + DP[l][i] + DP[i][r])
        pprint.pprint(DP)
        return DP[0][n-1]
            
print Solution().maxCoins_v3([3,1,5,8])