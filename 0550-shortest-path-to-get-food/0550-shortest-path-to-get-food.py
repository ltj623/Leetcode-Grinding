class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "*":
                    q.append((r,c,0))
                    break
            if q:break
        
        while q:
            row, col, count = q.popleft()
            if grid[row][col] == "X": continue
            if grid[row][col] == "#": return count
            grid[row][col] = "X"
            direct = ((1,0),(-1,0),(0,1),(0,-1))
            for dr, dc in direct:
                r, c = row + dr, col + dc
                if r in range(rows) and c in range(cols) and grid[r][c] != "X":
                    q.append((r,c,count+1))
        return -1


        