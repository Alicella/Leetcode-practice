import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Recursion: O(nlogn):   
        return self.maxSubArrayHelper(nums, 0, len(nums) - 1)
       
    def maxSubArrayHelper(self, nums, low, high):
        if low == high:                 # base case
            return nums[low]

        mid = low + (high - low) // 2

        leftMax = self.maxSubArrayHelper(nums, low, mid)
        rightMax = self.maxSubArrayHelper(nums, mid + 1, high)
        midMax = self.maxSubArrayMiddle(nums, low, mid, high)
        
        return max(leftMax, rightMax, midMax)
        
    def maxSubArrayMiddle(self, nums, low, mid, high):
        leftSum = -math.inf
        currSum = 0
        for i in range(mid, low - 1, -1):
            currSum += nums[i]
            leftSum = max(leftSum, currSum)

        rightSum = -math.inf
        currSum = 0
        for j in range(mid + 1, high + 1):
            currSum += nums[j]
            rightSum = max(rightSum, currSum)

        return leftSum + rightSum
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # O(n) DP/sliding window
#         max_sum = nums[0]
#         current_sum = nums[0]
        
#         for num in nums[1:]:
#             current_sum = max(num, current_sum + num)
            
#             if current_sum > max_sum:
#                 max_sum = current_sum
        
#         return max_sum
        
        
            