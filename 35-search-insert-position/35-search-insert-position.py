class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums_cp = nums.copy()
        while len(nums_cp) > 1:
            half = len(nums_cp)//2
            middle = nums_cp[half]
            
            if target < middle:
                del nums_cp[half:]
            elif target > middle:
                del nums_cp[:half]
            else:
                return nums.index(middle)
        
        # if the target isn't in the array:
        last_el = nums_cp[0]
        if target > last_el:
            return nums.index(last_el) + 1
        else:
            return nums.index(last_el)
                
        