class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # https://www.youtube.com/watch?v=pV2kpPD66nE&list=RDLVpV2kpPD66nE&index=1         #  BFS
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        
        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))       #add the visited cell as a tuple
            q.append((r, c))
            
            while q:
                row, col = q.popleft()       # if q.pop, then DFS???
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and
                        grid[r][c] == '1' and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands
                        
        
        
        
        
        
        
        
        
        
        
        
        # https://leetcode.com/problems/number-of-islands/discuss/56340/Python-Simple-DFS-Solution
        # DFS:    不懂
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
        
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'    # mark as visited?
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        