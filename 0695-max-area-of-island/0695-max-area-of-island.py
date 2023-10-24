class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c, grid):
            if r not in range(rows) or c not in range(cols) or grid[r][c] != 1:
                return 0

            islands = 1
            grid[r][c] = '*'

            islands += dfs(r+1,c,grid)
            islands += dfs(r-1,c,grid)
            islands += dfs(r,c+1,grid)
            islands += dfs(r,c-1,grid)

            return islands
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res, dfs(r,c,grid))
        return res