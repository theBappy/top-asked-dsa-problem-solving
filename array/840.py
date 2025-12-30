class Solution:
    def isMagicGrid(self, grid: List[List[int]], r: int, c: int) -> bool:
        # uniqueness 1 to 9 and distinct
        st = set()
        for i in range(3):
            for j in range(3):
                num = grid[r + i][c + j]
                if num < 1 or num > 9 or num in st:
                    return False
                else:
                    st.add(num)

        # check Sum - Rows and columns
        SUM = grid[r][c] + grid[r][c + 1] + grid[r][c + 2]
        for i in range(3):
            if (grid[r + i][c] + grid[r + i][c + 1] + grid[r + i][c + 2]) != SUM:
                return False

            if (grid[r][c + i] + grid[r + 1][c + i] + grid[r + 2][c + i]) != SUM:
                return False

        # diagonal and anti-diagonal
        if (grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2]) != SUM:
            return False

        if (grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c]) != SUM:
            return False

        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        count = 0

        for i in range(rows - 2):
            for j in range(cols - 2):
                if self.isMagicGrid(grid, i, j):
                    count += 1

        return count