# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []
                
        def dfs(root, path):
            """Inorderly traverse the tree, add each node to a list"""
            nonlocal res
            
            if not root:
                return
            
            path += str(root.val)
            
            if not root.left and not root.right:
                res.append(path)
            
            dfs(root.left, path + '->')
            dfs(root.right, path + '->')
        
        dfs(root, '')
        
        return res
            
            # if not root:
            #     paths.append(dfs(root))
            #     return []
            # elif root.left:
            #     return [str(root.val)] + dfs(root.left)
            # elif root.right:
            #     return [str(root.val)] + dfs(root.right)
        
#         res = []
#         for l in paths:
#             l = '->'.join(l)
#             res.append(l)
        
#         return res

            
            
                
        
        
            
            
        