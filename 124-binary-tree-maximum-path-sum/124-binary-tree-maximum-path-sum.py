# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Reference: https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
        """
        max_sum = root.val
        
        #inorder traversal
        def get_max_gain(root):
            nonlocal max_sum
            
            if not root:
                return 0
            
            left_gain = max(get_max_gain(root.left), 0) 
            right_gain = max(get_max_gain(root.right), 0)
            cur_sum = root.val + left_gain + right_gain
            
            max_sum = max(max_sum, cur_sum)
            
            return root.val + max(left_gain, right_gain)
        
        get_max_gain(root)
        
        return max_sum
        
        