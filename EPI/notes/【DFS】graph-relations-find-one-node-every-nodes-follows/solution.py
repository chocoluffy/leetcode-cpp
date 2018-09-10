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

- graph中的关注关系想成是有向图。相互关注会形成一个个strongly connected component, 由SCC组成的DAG中，去找最终出度为0的点，如果由多个则该题无法解答，如果只有一个出度为0的点，则该SCC点里所有的点，都可以被其他所有点所连通到，也就是题目中提到的抖音红人。
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
        if g[y][k] == 1 and g[x][k] == 0 and visited[k] == False:
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
