import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [0] * (n+1)
        for i in xrange(1, n+1):
            tmp = float('inf')
            for j in xrange(1, int(math.sqrt(i)) + 1):
                tmp = min(tmp, table[i - j**2] + 1)
            table[i] = tmp
        print table
        return table[n]
        
print Solution().numSquares(12)