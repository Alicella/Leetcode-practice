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
        self.found = False
        
        def dfs(root, curSum):
            if not root:
                return
            curSum += root.val
            if not root.left and not root.right:
                if curSum == targetSum:
                    self.found = True
                    return
                curSum -= root.val
                
            dfs(root.left, curSum)
            dfs(root.right, curSum)
        
        dfs(root, 0)
        return self.found
        
        
#         if not root:
#             return False
#         self.paths = []
        
#         def dfs(root, curSum):
#             # traverse a root to a leaf, updating curSum
            
#             if not root:                    #how to return without returning false
#                 return
#             curSum += root.val
#             # print(curSum)
#             if not root.left and not root.right:
#                 self.paths.append(curSum)
#                 curSum -= root.val               
#             dfs(root.left, curSum)
#             dfs(root.right, curSum)
        
#         dfs(root, 0)
#         if targetSum in self.paths:
#             return True
#         return False
        
                
                