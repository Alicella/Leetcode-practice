class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # NO.1 use list insert method:
        # O(n * k)
      
        for i in range(-1, -k - 1, -1):
            rotated_el = nums.pop()
            nums.insert(0, rotated_el)
        
        