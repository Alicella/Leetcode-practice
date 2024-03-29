class Solution:
    def search(self, nums: List[int], target: int) -> int:
#         low, high = 0, len(nums) - 1
        
#         while low <= high:
#             mid = (low + high) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 low = mid + 1              
#             else:
#                 high = mid - 1
        
#         return -1
        
        def bs(low, high):
            if low > high:
                return -1
            
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return bs(mid + 1, high)
            else:
                return bs(low, mid - 1)
         
        return bs(0, len(nums) - 1)
        
        
        
        
        
        
        
        # initialize the boundaries
#         lo = 0
#         hi = len(nums) - 1
        
#         while lo <= hi:
#             mid = lo + (hi - lo) // 2    # !!!
#             if target == nums[mid]:
#                 return mid
#             elif target < nums[mid]:
#                 hi = mid - 1
#             else:
#                 lo = mid + 1

#         return -1
        
        # Recursive way:
        # mid = lo + (hi - lo) // 2
        # if target == nums[mid]:
        #     return mid
        # elif target < nums[mid]:
        #     hi = mid - 1
        #     return self.search(nums[lo:hi], target)
        # else:
        #     lo = mid + 1
        #     return self.search(nums[lo:hi], target)
    
        # why I didn't solve it the first time: 
        # 1) Forgot how to update index after resize the array
        
#         lo = 0
#         hi = len(nums) - 1
#         mid = (hi - lo) // 2   !!!!
#         if target == nums[mid]:
#             return mid
#         elif target < nums[mid]:
#             hi = mid
#             return self.search(nums[0:mid], target)
#         else:
#             lo = mid
#             return self.search(nums[mid:], target)

#         return -1