class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        i = 0
        while i < n:
            if nums[i] == 0:
                nums.insert(len(nums), 0)
                nums.pop(i)
                n -= 1
            else:
                i += 1
                
                
        
        
        # for i in range(len(nums) - 1):
        #     if nums[i] == 0:
        #         k = 1
        #         while i + k < len(nums):
        #             if nums[i + k] != 0:
        #                 nums[i] = nums[i + k]
        #                 nums[i + k] = 0
        #                 break
        #             k += 1