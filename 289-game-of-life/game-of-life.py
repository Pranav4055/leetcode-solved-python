class Solution(object):
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                c = 0
                for x in range(max(0, i-1), min(m, i+2)):
                    for y in range(max(0, j-1), min(n, j+2)):
                        if (x, y) != (i, j) and board[x][y] % 2 == 1:
                            c += 1

                if board[i][j] % 2 == 1:
                    if c == 2 or c == 3:
                        board[i][j] = 3
                elif c == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                board[i][j] //= 2