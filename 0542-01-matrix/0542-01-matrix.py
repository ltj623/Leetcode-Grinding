class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        visited = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        
        while q:
            r, c = q.popleft()
            direct = ((1,0),(-1,0),(0,1),(0,-1))
            for dr, dc in direct:
                row,col = r + dr, c + dc
                if row in range(rows) and col in range(cols) and (row, col) not in visited:
                    mat[row][col] = mat[r][c] + 1
                    q.append((row,col))
                    visited.add((row,col))
        return mat