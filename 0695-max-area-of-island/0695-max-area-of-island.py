class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = []
        max_area = 0
        
        # O(m*n)
        def dfs(r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1 and (r, c) not in visited:
                visited.append((r,c))
                return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
            else:
                return 0
          
         
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(dfs(r, c), max_area)
    
        return max_area
        