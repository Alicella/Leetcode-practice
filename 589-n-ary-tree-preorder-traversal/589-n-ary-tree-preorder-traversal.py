"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        # iterative way is to use queue/stack
        output = []
        if not root: return
        q = deque([root])      
        
        while q:
            cand = q.popleft()
            output.append(cand.val)
            
            # if not reverse and add children in order, 
            # will become BFS
            for c in reversed(cand.children):
                q.appendleft(c)
        
        return output
        
        
        # recursive way is similar to solving binary trees problems
        output = []
        def dfs(node):
            if not node: return
            
            output.append(node.val)
            for c in node.children:
                dfs(c)
            
        dfs(root)
        
        return output

        