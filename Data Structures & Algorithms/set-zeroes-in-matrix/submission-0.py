class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        row_zero = False
        col_zero = False

        # Check if first row contains a zero
        for j in range(cols):
            if matrix[0][j] == 0:
                row_zero = True

        # Check if first column contains a zero
        for i in range(rows):
            if matrix[i][0] == 0:
                col_zero = True

        # Use first row and first column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero rows based on markers
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0

        # Zero columns based on markers
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0

        # Zero the first row if necessary
        if row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero the first column if necessary
        if col_zero:
            for i in range(rows):
                matrix[i][0] = 0