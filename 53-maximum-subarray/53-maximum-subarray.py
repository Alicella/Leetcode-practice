class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -99999
        cur_sum = 0
        
        for num in nums:
            cur_sum += num
            
            if cur_sum > max_sum:
                max_sum = cur_sum
            
            if cur_sum < 0:     # adding negative numbers will reduce the sum
                cur_sum = 0
        return max_sum
        