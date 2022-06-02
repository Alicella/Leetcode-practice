# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
 
        else:
            return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))
        
#         queue = []
#         queue.append((root.left, root.right))
        
#         while queue:
#             l, r = queue.pop(0)
#             if not l:
#                 l = r
#                 # queue.append((l.left, l.right))
#             elif not r:
#                 r = l
#                 # queue.append((r.left, r.right))
#             else:
#             # tmp = l
#             # l = r
#             # r = tmp
#                 l, r = r, l
#                 queue.append((l.left, l.right))
#                 queue.append((r.left, r.right))
  
#         return TreeNode(queue)
                
                
            
            
            
            
            
            
            
            
            
            
            