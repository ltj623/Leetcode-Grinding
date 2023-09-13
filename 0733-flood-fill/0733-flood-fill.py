class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r, c = len(image), len(image[0])
        orig_color = image[sr][sc]
        if color == orig_color: return image

        def dfs(i, j):
            if (i < 0 or i >= r or j < 0 or j >= c or image[i][j] != orig_color or image[i][j] == color): return
            if image[i][j] == orig_color:
                image[i][j] = color
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        dfs(sr, sc)
        return image

        