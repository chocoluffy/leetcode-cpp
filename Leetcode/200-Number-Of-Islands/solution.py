"""
典型题：
- DFS的空间复杂度是O(N*M)，因为worst case是全部都为1，这个时候的stack number为
  O(N*M)，即便我们可以直接修改原grid而不额外引入复杂度，因为function call引入的
  复杂度是需要考虑进去的。

> 原本写有visited[N][M]的算法会给runtime error(recursion depth exceeds)，但是由
于可以直接修改参数grid，使得不需要extra的visited来记录哪些path是经过的。

仔细思考一下为什么这个修改会改善程序：
- 因为stack frame会包括global variables!因此当grid size特别大的时候，每一个
  function call的stack也会大，导致depth exceeds。
"""
class Solution(object):
    # runtime error in LeetCode, as it exceeds the stack limit.
    def numIslands(self, grid):
        """
        :type grid: List[List[str]] :rtype: int
        """
        # in main function, accmulate the counter whenever reaches 1. then go
        # DFS in all valid directions and mark all visited node in False. 
        n = len(grid)
        m = len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def valid_pos(x, y):
            return 0 <= x < n and 0<= y < m
        def dfs(x, y):
            visited[x][y] = True
            for d in directions:
                new_x = x + d[0]
                new_y = y + d[1]
                if valid_pos(new_x, new_y) and visited[new_x][new_y] == False:
                    dfs(new_x, new_y)
        visited = [[False] * m for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == False and grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j)
        return cnt
    
    # accepted.
    def numIslands_v2(self, grid):
        """
        :type grid: List[List[str]] :rtype: int
        """
        # in main function, accmulate the counter whenever reaches 1. then go
        # DFS in all valid directions and mark all visited node in False. 
        if not grid or not grid[0]:
            return 0
        n = len(grid)
        m = len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def valid_pos(x, y):
            return 0 <= x < n and 0<= y < m
        def dfs(x, y):
            grid[x][y] = 0
            for d in directions:
                new_x = x + d[0]
                new_y = y + d[1]
                if valid_pos(new_x, new_y) and grid[new_x][new_y] == "1":
                    dfs(new_x, new_y)
        # visited = [[False] * m for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j)
        return cnt

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print Solution().numIslands(grid)
                
