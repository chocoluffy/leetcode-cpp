"""
和头条OA最后一道题很像，但是头条是单向的，Linkedin这道题是双向的。
"""
def zombieCluster(zombies):
    grid = []
    for l in zombies:
        new_l = list(l)
        grid.append(new_l)
    if not grid or not grid[0]:
        return 0
    n = len(grid)
    def valid_pos(x, y):
        return 0 <= x < n and 0<= y < n
    def dfs(x, y):
        grid[x][y] = 0
        for i in range(n):
            if grid[x][i] == "1":
                grid[x][i] = 0
                grid[i][x] = 0
                dfs(i, i)
    cnt = 0
    for i in xrange(n):
        if grid[i][i] == "1":
            cnt += 1
            dfs(i, i)
    return cnt

data = [
    "10100",
    "01000",
    "10100",
    "00010",
    "00001"
]
print zombieCluster(data)