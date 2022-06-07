# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # need a helper func to count nodes
        # if left subtree has >=k nodes, then it has that node (else root or rightsub)
        # the root is the kth node when its left seubtree has k-1 nodes or 
        # all parts in its left has k-1 nodes
        def count_node(root):
            """count the nodes during the inorder traversal
               return the number of nodes"""
            if not root:
                return 0
            else:
                return 1 + count_node(root.left) + count_node(root.right)
        
        while root:
            left_counts = count_node(root.left)
            if left_counts == k-1:
                return root.val
            elif left_counts > k-1:
                root = root.left
            else:
                k = k - left_counts - 1
                root = root.right
              
            
            
            
        
        
        