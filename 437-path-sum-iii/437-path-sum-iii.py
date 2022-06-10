# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        # intuitive, O(n2)
        def pathSum_r(root, targetSum):
            if not root:
                return 0
            res = 0
            if root.val == targetSum: res += 1
                
            res += pathSum_r(root.left, targetSum - root.val)
            res += pathSum_r(root.right, targetSum - root.val)
            return res
        
        if not root:
            return 0
        
        return self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum) + pathSum_r(root, targetSum)
        
        
        
        
        