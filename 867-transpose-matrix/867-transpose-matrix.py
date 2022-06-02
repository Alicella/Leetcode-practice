class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        
        new_mx = []
        
        width = len(matrix[0])
        height = len(matrix)
        
        for i in range(width):
            new_row = []
            for j in range(height):
                new_row.append(matrix[j][i])
            new_mx.append(new_row)
        
        return new_mx
            