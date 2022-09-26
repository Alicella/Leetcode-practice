# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # O(log n) running time
        if not root:
            return 
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        mi = min(p.val, q.val)
        ma = max(p.val, q.val)
        
        if root.val < mi:
            return right
        elif root.val > ma:
            return left
        else:
            return root
            