# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = []
        count = 0
        queue.append((root.left, root.right))    # first: append the whole left subtree and the whole right subtree
        # print('original', queue)
        while queue:
            l, r = queue.pop(0)
            # print('---l---',l, '---r---',r)
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            queue.append((l.left, r.right))
            queue.append((l.right, r.left))
            count += 1
            # print(str(count), queue)
        return True
        
        
#         if not root:
#             return True
    
#         queue = [root]
        
#         while len(queue) > 0:
#             cur_node = queue.pop(0)
#             if cur_node.left:
#                 queue.append(cur_node.left)
#             if cur_node.right:
#                 queue.append(root.right)
            
#             for i in range(len(queue)):
#                 if queue[i].val != queue[len(queue) - 1 - i].val:
#                     return False
        
#         return True     
    
    
                
                