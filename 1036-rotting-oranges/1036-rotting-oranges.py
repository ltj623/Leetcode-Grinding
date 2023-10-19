class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                direct = ((1,0),(-1,0),(0,1),(0,-1))
                for dr, dc in direct:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r,c))
            time += 1

        return time if fresh == 0 else -1  
                    

        