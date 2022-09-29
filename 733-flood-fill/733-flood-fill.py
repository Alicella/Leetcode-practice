class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
           
        m, n = len(image), len(image[0])
        
        color = image[sr][sc]
        
        if color == new_color:    # That's the base case, not 1 pixel
            return image
        
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = new_color
                if r - 1 >= 0: dfs(r-1, c)
                if r + 1 < m: dfs(r+1, c)
                if c - 1 >= 0: dfs(r, c-1)
                if c + 1 < n: dfs(r, c+1)
        
        dfs(sr, sc)
        return image
        