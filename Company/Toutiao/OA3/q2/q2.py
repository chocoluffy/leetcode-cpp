lines = int(raw_input())
grid = []
for _ in range(lines):
    row = map(int, raw_input().strip().split(' '))
    grid.append(row)

def dfs(grid):
    if not grid or not grid[0]:
        return 0
    else:
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
                if valid_pos(new_x, new_y) and grid[new_x][new_y] == 1:
                    dfs(new_x, new_y)

        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cnt += 1
                    dfs(i, j)
        return cnt

print dfs(grid)