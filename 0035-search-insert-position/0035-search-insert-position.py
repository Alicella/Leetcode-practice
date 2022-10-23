class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low, high = 0, len(nums) - 1
        mid = low + (high - low) // 2
        
        while high - low > 1:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        # low < tgt < high and low + 1 = high, so insert at high
        return high
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      
#         nums_cp = nums.copy()
#         while len(nums_cp) > 1:
#             half = len(nums_cp)//2
#             middle = nums_cp[half]
            
#             if target < middle:
#                 del nums_cp[half:]
#             elif target > middle:
#                 del nums_cp[:half]
#             else:
#                 return nums.index(middle)
        
#         # if the target isn't in the array:
#         last_el = nums_cp[0]
#         if target > last_el:
#             return nums.index(last_el) + 1
#         else:
#             return nums.index(last_el)
                
# better(neater) solution from discussion https://leetcode.com/problems/search-insert-position/discuss/1979595/JavaC%2B%2BPythonKotlinJavaScript-2LINES-O(n)timeBEATS-99.97-MEMORYSPEED-0ms-APRIL-2022
    def searchInsert(self, nums, target):
        i = 0
        j = len(nums) - 1
        while(i <= j):
            pivot = (i + j) // 2                # better binary search method
            if (nums[pivot] == target):
                return pivot
            elif (nums[pivot] > target):
                j = pivot - 1                   # shorten the list without making a copy or actually deleting
                                                # sections of the list, just negelect the rest
            else:
                i = pivot + 1
        return i                                # only need to return i!!! if the target < left end, i remain 0;
                                                # elif the target > right end, i will be j + 1
                                                