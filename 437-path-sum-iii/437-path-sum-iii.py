# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        # use hash table/dictionary
        # two tutorials: https://www.youtube.com/watch?v=VDTZiggKlAE      https://www.youtube.com/watch?v=KvLzxCHnu_A
        count = 0
        prefixSum = defaultdict(int) 
        prefixSum[0] = 1
        
        def dfs(root, curSum):
            nonlocal count                  # why prefixSum doesn't need to be nonlocal
            if not root: return
            
            curSum += root.val
            # print(curSum)
            if curSum - targetSum in prefixSum:
                count += prefixSum[curSum - targetSum]
                
            prefixSum[curSum] += 1          
            # print(prefixSum)  
            
            dfs(root.left, curSum)
            dfs(root.right, curSum)
            
            prefixSum[curSum] -= 1
        
        dfs(root, 0)
        
        return count
   
        
        
        
        
        # intuitive, O(n2)
#         def pathSum_r(root, targetSum):
#             if not root: return 0
#             res = 0
#             if root.val == targetSum: res += 1
#             res += pathSum_r(root.left, targetSum - root.val)
#             res += pathSum_r(root.right, targetSum - root.val)
#             return res
        
#         if not root: return 0
#         return self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum) + pathSum_r(root, targetSum)
        
        
        
        
        