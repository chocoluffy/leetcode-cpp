"""
DFS version straigtforward.

BFS version: 

for i in range(n):
	if not visited:
    	add to queue.
        while queue not empty:
        	for loop append all connected points to queue.
            ...
        count += 1

"""
# DFS version.
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