# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.paths = []
        
        def dfs(root, curSum):
            # traverse a root to a leaf, updating curSum
            
            if not root:                    #how to return without returning false
                return
            curSum += root.val
            # print(curSum)
            if not root.left and not root.right:
                self.paths.append(curSum)
                curSum -= root.val
                
            dfs(root.left, curSum)
            dfs(root.right, curSum)
        
        dfs(root, 0)
        if targetSum in self.paths:
            return True
        
        return False
        
    
    
    
    
    
    
    
#         curSum = 0
#         leaves = []
#         if root:
#             curSum += root.val
#             if not root.left and not root.right:
#                 # print('leaf', curSum)
#                 if curSum == targetSum:
#                     leaves.append(root.val)
#                     return True
#                 else:
#                     curSum -= root.val
        
#         self.hasPathSum(root.left, targetSum)
#         self.hasPathSum(root.right, targetSum)

                
                