# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        
        # find the rightmost leaf/tail of the left subtree
        if root.left:
            self.flatten(root.left)      #--------KEY!!!------
            
            
            tail = root.left
            while tail.right:
                tail = tail.right

            # add the right subtree to this leaf/tail
            tail.right = root.right
            print('cur tail', tail) 
            
            # move the flattened left subtree to right
            root.right = root.left
            root.left = None

            print('cur_root', root)

        self.flatten(root.right)
            
            
            
            
            
            
            
            
            
            
            
            