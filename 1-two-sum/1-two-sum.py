

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        output = []
        for i in range(len(nums)):
            if nums[i] not in res.values():
                res[nums[i]] = target - nums[i]
            else:
                output.append(i)
                for k, v in res.items():
                    if v == nums[i]:
                        output.append(k)
        
        return output


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#discussion: https://leetcode.com/problems/two-sum/discuss/1979527/JavaC%2B%2BPythonO(n)timeBEATS-99.97-MEMORYSPEED-0ms-APRIL-2022   
# the idea is Hashmap.
class Solution:
    def twoSum(self, nums, target):
        values = {}
        for i, num in enumerate(nums):
            remaining = target - num         #with the current num, know the target solution
            if remaining in values:                # you find the only solution with the current num 
                                                   # plus the previous num stored in the values dictionary.
                
                return [i, values[remaining]]     # the result is in reverse order
                                                    
            else:
                values[num] = i            # dictionary's key is num, value is its index    
                






