# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def collect_node(root):
#             # """ Turn a tree into a list of nodes values"""           
#             if not root:
#                 return []
#             elif not root.left and not root.right:
#                 return [root.val]
#             else:
#                 return collect_node(root.left) + [root.val] + collect_node(root.right)

#         if not root:
#             return True
#         elif root.left and max(collect_node(root.left)) >= root.val:
#             print('root, root.left', root.val, root.left.val)
#             return False
#         elif root.right and min(collect_node(root.right)) <= root.val:
#             print('root, root.rightt', root.val, root.right.val)
#             return False
#         else:
#             return self.isValidBST(root.left) and self.isValidBST(root.right)
            
        def validate(root, low = -math.inf, high = math.inf):
            if not root:
                return True
            elif root.val <= low or root.val >= high:
                return False
            
            return (validate(root.left, low, root.val)) and (validate(root.right, root.val, high))
    
        return validate(root)
        