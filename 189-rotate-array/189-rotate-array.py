class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # NO.1 use list insert method:
        
        i = -1 
        while i >= -k:
            rotated_el = nums.pop()
            nums.insert(0, rotated_el)
            i -= 1