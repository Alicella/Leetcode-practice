class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # intuitive solutoin:
        # build a list of squared nums, then sort the new list
        
        # square = nums.copy()
        # for i in range(len(square)):
        #     square[i] = nums[i] * nums[i]    
        # square.sort()         # O(nlogn)!!!!!!!!!!!!!!!!
        # return square
        
        # Two pointers: 
        # Abs values of nums is "V" shape, or "\" or "/" shape
        # compare and insert the left and right most nums ^2 in order
        # l and r move inwards---- once a time!!!

            
       
        l = 0
        r = len(nums) - 1
        w = len(nums) - 1    # the writing pointer
        square = [0] * len(nums)
        
        while w >= 0:
            if abs(nums[l]) > abs(nums[r]):
                square[w] = nums[l] ** 2
                l += 1
            else:
                square[w] = nums[r] ** 2
                r -= 1
            w -= 1
        
        return square

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            