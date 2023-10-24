class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()

        def bfs(r,c):
            q.append((r,c))
            visited.add((r,c))

            islands = 1
            while q:
                row, col = q.popleft()
                direct = ((1,0),(-1,0),(0,1),(0,-1))
                for dr, dc in direct:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] == 1:
                        q.append((r,c))
                        visited.add((r,c))
                        islands += 1
            return islands
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    res = max(res, bfs(r,c))
        return res
        