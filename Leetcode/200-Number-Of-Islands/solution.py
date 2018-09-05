class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # in main function, accmulate the counter whenever reaches 1. then go DFS in all valid directions and mark all visited node in False. 
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

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print Solution().numIslands(grid)
                
