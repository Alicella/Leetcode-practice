# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """Return a list of paths, each path a list of node values"""
        # dfs needs to go through every node
        
        self.paths = []
        
        def dfs(root, targetSum, curPath):
            # traverse a root to a leaf, updating curSum and curPath
            
            if not root:                    
                return
            # curSum += root.val
            curPath.append(root.val)
            
            if not root.left and not root.right:    # Arriving at a leaf
                # if curSum == targetSum: 
                if root.val == targetSum:
                    self.paths.append(curPath[:])
                # whether find the target sum or not, need to remove this leaf node
                # curSum -= root.val
                # curPath.pop()
            else:
                dfs(root.left, targetSum - root.val, curPath)
                dfs(root.right, targetSum - root.val, curPath)
            curPath.pop()
        
        dfs(root, targetSum, [])
        return self.paths
        