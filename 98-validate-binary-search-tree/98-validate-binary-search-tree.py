# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         output =[]
#         self.inorder(root, output)
        
#         for i in range(1, len(output)):
#             if output[i-1] >= output[i]:
#                 return False
        
#         return True
    
#     # Time complexity of inorder traversal is O(n)
#     # Fun fact: Inorder traversal leads to a sorted array if it is 
#     # a Valid Binary Search. Tree.
#     def inorder(self, root, output):
#         if root is None:
#             return
        
#         self.inorder(root.left, output)
#         output.append(root.val)
#         self.inorder(root.right, output)
        output = []
        self.in_tr(root, output)
        for i in range(1,len(output)):
            if output[i] <= output[i - 1]:
                return False
        return True
        
        
    def in_tr(self, root, output = []):        # !!!This is simply inorder traversal!!!
        # """ Turn a tree into a list of nodes values"""           
        if not root:
            return []
        else:
            self.in_tr(root.left, output)
            output.append(root.val)
            self.in_tr(root.right, output)

        
            
            
            
#         
#         else:
#             return self.isValidBST(root.left) and self.isValidBST(root.right)
            
#         def validate(root, low = -math.inf, high = math.inf):
#             if not root:
#                 return True
#             elif root.val <= low or root.val >= high:
#                 return False
            
#             return (validate(root.left, low, root.val)) and (validate(root.right, root.val, high))    
    
#         return validate(root)
        