class Solution(object):
    # DFS version.
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) > 0 and len(board[0]) > 0:
            N = len(board)
            M = len(board[0])
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            def dfs(board, x, y):
                board[x][y] = 'T'
                for d in directions:
                    new_x = x + d[0]
                    new_y = y + d[1]
                    if 0 <= new_x < N and 0 <= new_y < M and board[new_x][new_y] == 'O':
                        dfs(board, new_x, new_y)

            for i in [0, N-1]:
                for j in range(M):
                    if board[i][j] == 'O':
                        dfs(board, i, j)

            for i in [0, M-1]:
                for j in range(N):
                    if board[j][i] == 'O':
                        dfs(board, j, i)

            for i in range(N):
                for j in range(M):
                    if board[i][j] == 'T':
                        board[i][j] = 'O'
                    elif board[i][j] == 'O':
                        board[i][j] = 'X'
    
    # union find version.
    def solve_v2(self, board):


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(board)
print board