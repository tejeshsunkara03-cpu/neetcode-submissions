class Solution:
    def solve(self, board):

        if not board:
            return

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if board[r][c] != 'O':
                return

            board[r][c] = '#'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Check left and right borders
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        # Check top and bottom borders
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Capture surrounded regions
        for r in range(rows):
            for c in range(cols):

                if board[r][c] == 'O':
                    board[r][c] = 'X'

                elif board[r][c] == '#':
                    board[r][c] = 'O'