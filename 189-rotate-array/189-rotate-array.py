class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # No.3 rotate left by n-k steps?

        n = len(nums)
        if n > k:
            for i in range(n - k):
                nums.append(nums.pop(0))
        else:
           # in the first k // n times,
           # rotating just doesn't make change to nums.
           # actual_rotation = k % n
            for i in range(n - k % n):
                nums.append(nums.pop(0))
        
        
        
        # No.2 use collection.deque... doesn't work
        # created a copy to the reference?
#         nums = collections.deque(nums)
#         for i in range(k):
#             rotated_el = nums.pop()
#             nums.appendleft(rotated_el)
        
#         nums = list(nums)
        
        
        
        # No.1 use list insert method:
        # O(n * k)
      
        # for i in range(-1, -k - 1, -1):
        #     rotated_el = nums.pop()
        #     nums.insert(0, rotated_el)
        
        
    
        