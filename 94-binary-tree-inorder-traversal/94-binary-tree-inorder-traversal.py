# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
# discussion https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/?currentPage=1&orderBy=most_votes&query=&tag=python
#         return self.helper(root, [])
    
#     def helper(self, root, res):
#         if root:
#             self.helper(root.left, res)
#             res.append(root.val)
#             self.helper(root.right, res)
#         return res
        

        
           
    
    
