class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        # O(m*n) time, O(1)space
        
        rows, cols = len(mat), len(mat[0])
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else math.inf
                    left = mat[r] [c - 1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1
            
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < rows - 1 else math.inf
                    right = mat[r][c + 1] if c < cols - 1 else math.inf
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)
        
        return mat
        
        
        
        
        
        
        
        
        
        
        
        
        
        # O(m * n) time and space
        rows, cols = len(mat), len(mat[0])
        DIR = [0, 1, 0, -1, 0]
        
        q = deque([])
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1   # marked as unprocessed
            
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if nr < 0  or nr == rows or nc < 0 or nc == cols or mat[nr][nc] != -1:
                    continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr,nc))
        
        return mat
        
        