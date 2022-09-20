class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            left_sum = sum(nums[0:i])
            right_sum = sum(nums[i+1:])
            if left_sum == right_sum:
                return i
            elif i == 0 and right_sum == 0:
                return 0
            
        return -1