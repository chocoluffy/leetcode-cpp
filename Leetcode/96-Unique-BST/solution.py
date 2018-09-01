class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        UBST = [0] * (n+1)
        UBST[0] = UBST[1] = 1
        for i in xrange(2, n+1):
            for j in xrange(1, i+1):
                UBST[i] = UBST[i] + (UBST[j-1] * UBST[i-j])
        return UBST[n]