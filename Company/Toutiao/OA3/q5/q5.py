N = int(raw_input())
M = int(raw_input())
lst = map(int, raw_input().strip().split(' '))
pairs = [[lst[i], lst[i+1]] for i, d in enumerate(lst) if i % 2 == 0]
print pairs
grid = [[False] * N for _ in range(N)]