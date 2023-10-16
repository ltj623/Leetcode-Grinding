class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        
        def bfs(r, c):
            q.append((r,c))
            visited.add((r,c))
            while q:
                r, c = q.popleft()
                direct = ((-1,0), (1,0), (0,1), (0,-1))
                for dr, dc in direct:
                    row, col = r + dr, c + dc
                    if row in range(rows) and col in range(cols) and (row, col) not in visited and grid[row][col] == "1":
                        q.append((row, col))
                        visited.add((row, col))
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    res += 1
        return res
        