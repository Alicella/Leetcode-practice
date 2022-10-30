class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # visited = []     seems like use a set() in this case is faster
        visited = set()
        max_area = 0
        m, n = len(grid), len(grid[0])
        
        
        def dfs(r, c):
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r,c))
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)     # !!!!!!!!!!
        
        # O(m*n)
        for r in range(m):
            for c in range(n):
                max_area = max(dfs(r, c), max_area)
    
        return max_area
        