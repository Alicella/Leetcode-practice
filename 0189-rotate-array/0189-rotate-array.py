class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # O(k) * O(n)
        # for _ in range(k):
        #     last = nums.pop()
        #     nums.insert(0, last)
            
        n = len(nums)
        k = k % n
        
        # move the first (n-k) elements to back
        for _ in range(n - k):
            first = nums.pop(0)
            nums.append(first)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # No.5 use reverse method with O(1) space and O(n) runtime‘
         
#         n = len(nums)
#         k = k % n
        
#         self.reverse(nums, 0, n - 1)
#         self.reverse(nums, 0, k - 1)
#         self.reverse(nums, k, n - 1)        
        
#     def reverse(self, nums, start, end):
#         l = start
#         r = end
#         while l < r:
#             nums[l], nums[r] = nums[r], nums[l]
#             l, r = l + 1, r - 1
              
        
        # No.4 use slicing 
        # reference: https://leetcode.com/problems/rotate-array/discuss/54294/My-solution-by-using-Python
        # n = len(nums)
        # k = k % n
        # nums[:] = nums[n-k:] + nums[:n-k]
        # or below
        # nums[:] = nums[-k:] + nums[:-k] 
        
        
        # No.3 rotate left by n-k steps

        # n = len(nums)
        # if n > k:
        #     for i in range(n - k):
        #         nums.append(nums.pop(0))
        # else:
        #    # in the first k // n times,
        #    # rotating just doesn't make change to nums.
        #    # actual rotating to right is k % n times
        #     for i in range(n - k % n):
        #         nums.append(nums.pop(0))    
        
        
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
        
        
    
        