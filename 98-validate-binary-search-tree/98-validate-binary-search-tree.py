# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # helper function to check if node val is in defined range
        def checkNode(node, minVal, maxVal):
            if not node: return True
            
            if node.val <= minVal or node.val >= maxVal:
                return False
            else:
                return checkNode(node.left, minVal, node.val) and checkNode(node.right, node.val, maxVal)
        
        # base case : only 1 node
        if not root.left and not root.right: return True
        
        return checkNode(root.left, -2147483649, root.val) and checkNode(root.right, root.val, 2147483648)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
          
        output =[]
        self.inorder(root, output)
        
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False
        
        return True
    
    # Time complexity of inorder traversal is O(n)
    # Fun fact: Inorder traversal leads to a sorted array if it is 
    # a Valid Binary Search. Tree.
    def inorder(self, root, output):
        if root is None:
            return        
        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)

        
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:                
#         def validate(root, low = -math.inf, high = math.inf):
#             if not root:
#                 return True
#             elif root.val <= low or root.val >= high:
#                 return False
            
#             return (validate(root.left, low, root.val)) and (validate(root.right, root.val, high))    
    
#         return validate(root)
        