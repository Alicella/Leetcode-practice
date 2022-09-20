class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # total sum of the array:
        total = sum(nums)
        cur_sum = 0
        # at the pivot index,
        # its left sum == right sum == (total - pivot num) / 2
        for i in range(len(nums)):
            target_sum = (total - nums[i]) / 2
            if cur_sum == target_sum:
                return i
            cur_sum += nums[i]
            
        
        return -1
        
        
        
        
        # O(n^2) solution:
        # for i in range(len(nums)):
        #     left_sum = sum(nums[0:i])
        #     right_sum = sum(nums[i+1:])
        #     if left_sum == right_sum:
        #         return i
        #     elif i == 0 and right_sum == 0:
        #         return 0
        # return -1