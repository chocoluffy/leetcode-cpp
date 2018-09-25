class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        def dfs(x, M):
            for i in range(N):
                if not has_seen[i] and M[x][i] == 1:
                    has_seen[i] = True
                    dfs(i, M)
        has_seen = [False] * N
        circle_num = 0
        for i in range(N):
            if not has_seen[i]:
                circle_num += 1
                dfs(i, M)
        return circle_num