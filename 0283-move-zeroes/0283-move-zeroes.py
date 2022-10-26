class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l, r = 0, 1
        while r < len(nums):
            if nums[l] == 0 and nums[r] == 0:
                r += 1
            elif nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            elif nums[l] != 0 and nums[r] == 0:
                l += 1
                r += 1
            else:
                l += 2
                r += 2
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # https://www.youtube.com/watch?v=aayNRwUN3Do
        # l = 0
        # for r in range(len(nums)):
        #     if nums[r]:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l += 1
        
        
        # n = len(nums) - 1
        # i = 0
        # while i < n:
        #     if nums[i] == 0:
        #     #if met 0, insert 0 at the end, and remove 0 at the current position.... also dealing with two pointers
        #         nums.insert(len(nums), 0)
        #         nums.pop(i)
        #         n -= 1
        #     else:
        #         i += 1         
    
        
        # for i in range(len(nums) - 1):
        #     if nums[i] == 0:
        #         k = 1
        #         while i + k < len(nums):
        #             if nums[i + k] != 0:
        #                 nums[i] = nums[i + k]
        #                 nums[i + k] = 0
        #                 break
        #             k += 1