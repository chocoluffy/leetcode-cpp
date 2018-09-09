"""
Input:
3
3
1 2 2 1 2 3

N people
M pairs of following relations
M pairs of (i, j), meaning i follows j.

Output:
1

output the number of super people, who everyone follows.
"""
import pprint

N = int(raw_input())
M = int(raw_input())
lst = map(int, raw_input().strip().split(' '))
pairs = [[lst[i], lst[i+1]] for i, d in enumerate(lst) if i % 2 == 0]
grid = [[0] * N for _ in range(N)]
for i, j in pairs:
    grid[i-1][j-1] = 1

def dfs(g, x, y, visited):
    for k in range(N):
        if g[y][k] == 1 and visited[k] == False:
            g[x][k] = 1
            visited[k] = True
            dfs(g, x, k, visited)

for i in range(N):
    visited = [False] * N
    for j in range(N):
        if i == j:
            grid[i][j] = 1
            visited[i] = True
        elif grid[i][j] == 1 and visited[j] == False:
            dfs(grid, i, j, visited)

cnt = 0
for col in range(N):
    flag = True
    for row in range(N):
        if grid[row][col] == 0:
            flag = False
    if flag == True:
        cnt += 1

pprint.pprint(cnt)
