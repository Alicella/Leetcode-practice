# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        # https://www.youtube.com/watch?v=gcR28Hc2TNQ
        #https://www.youtube.com/watch?v=6ZnyEApgFYg
        # BFS uses queue (dfs usually uses stack)
        # so how to traverse with queue:
        
        output = []
        
        q = collections.deque()
        q.append(root)
        
        while q:
            qLen = len(q)  #!!! ensuring interation through one level at a time
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node: 
                    level.append(node.val)            
                    q.append(node.left)
                    q.append(node.right)
            
            if level:
                output.append(level)
                    
        return output
  