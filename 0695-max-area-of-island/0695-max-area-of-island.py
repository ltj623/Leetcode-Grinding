class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited =set()

        def bfs(r, c):
            q.append((r,c))
            visited.add((r,c))
            islands = 1
            while q:
                r, c = q.popleft()
                direct = ((-1,0), (1,0),(0,1),(0,-1))
                for dr, dc in direct:
                    row, col = r + dr, c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1 and (row,col) not in visited:
                        q.append((row, col))
                        visited.add((row, col))
                        islands += 1
            return islands
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    islands = bfs(r,c)
                    res = max(res, islands)
        return res

                    


        # rows, cols = len(grid), len(grid[0])
        # visited = set()
        # q = deque()
        # res = 0

        # def bfs(r, c):
        #     q.append((r,c))
        #     visited.add((r,c))
        #     islands = 1
        #     while q:
        #         row, col = q.popleft()
        #         direct = ((1,0),(-1,0),(0,1),(0,-1))
        #         for dr, dc in direct:
        #             r, c = row + dr, col + dc
        #             if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] == 1:
        #                 q.append((r,c))
        #                 visited.add((r,c))
        #                 islands += 1
        #     return islands

        # for r in range(rows):
        #     for c in range(cols):
        #         if (r,c) not in visited and grid[r][c] == 1:
        #             islands = bfs(r,c)
        #             res = max(res, islands)
        # return res


