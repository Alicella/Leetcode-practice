class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
           
        m, n = len(image), len(image[0])
        
        color = image[sr][sc]
        
        if color == new_color:    # That's the base case, not 1 pixel
            return image
        
        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and image[r][c] == color:
                image[r][c] = new_color
                
                dfs(r-1, c)
                dfs(r+1, c)
                dfs(r, c-1)
                dfs(r, c+1)
        
        dfs(sr, sc)
        return image
        