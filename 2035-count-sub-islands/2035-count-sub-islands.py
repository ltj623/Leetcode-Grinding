class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or grid2[r][c] != 1:
                return
            
            grid2[r][c] = 0
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and grid1[r][c] == 0:
                    dfs(r,c)
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    dfs(r,c)
                    res += 1
        return res
        

        