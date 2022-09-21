class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # Thinking:
        # build a list of squared nums, then sort the new list
        
        square = nums.copy()
        for i in range(len(square)):
            square[i] = nums[i] * nums[i]
        
        square.sort()
        
        return square