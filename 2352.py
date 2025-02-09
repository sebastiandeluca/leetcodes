# Equal Row and Column Pairs
# 35ms, 15.7MB
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        n = len(grid)
        rows = collections.Counter(tuple(row) for row in grid)

        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            count += rows[tuple(col)]
        return count
                