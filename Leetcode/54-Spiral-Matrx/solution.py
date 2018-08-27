# challenge: 
#  - handle the case when the current pointer go outbound.
class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_ptr = 0
        col_len, row_len = len(matrix), len(matrix[0])
        visited = [[False] * row_len for _ in range(col_len)]
        r = 0
        c = 0
        res = [matrix[r][c]]
        while True:
            next_r = r + directions[direction_ptr][0]
            next_c = c + directions[direction_ptr][1]
            print next_r, next_c
            if next_r < 0 or next_c < 0 or next_r >= row_len or next_c >= col_len: #  outside
                direction_ptr = (direction_ptr + 1) % 4
            elif visited[next_r][next_c]:
                return res
            else: # inside
                visited[next_r][next_c] = True
                res.append(matrix[next_r][next_c])
                r = next_r
                c = next_c

print Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8]])