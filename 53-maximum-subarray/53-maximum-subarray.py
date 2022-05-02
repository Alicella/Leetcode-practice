class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
# solution found in https://leetcode.com/problems/maximum-subarray/discuss/1947761/Python3-Simple-Approach-for-100-Faster
#         max_sum = -99999
#         cur_sum = 0
        
#         for num in nums:
#             cur_sum += num
            
#             if cur_sum > max_sum:
#                 max_sum = cur_sum
            
#             if cur_sum < 0:     # because adding negative numbers will reduce the sum
#                 cur_sum = 0
#         return max_sum

#a clearer one but same algotithm: https://leetcode.com/problems/maximum-subarray/discuss/1990093/Python-simple-iterative-solution-(Kadane's-algorithm)

#         max_sum = nums[0]
#         current_sum = 0
        
#         for num in nums:
#             if current_sum < 0:
#                 current_sum = 0
#             current_sum += num
            
#             max_sum = max(max_sum, current_sum)
        
#         return max_sum

# another solution: https://leetcode.com/problems/maximum-subarray/discuss/1913024/Python-Solution
        max_sum = nums[0]
        current_sum = nums[0]
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)        
        
        return max_sum
        
        
            