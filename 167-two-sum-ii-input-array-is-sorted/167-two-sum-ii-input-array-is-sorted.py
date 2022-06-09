class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # loop through the list, for each element, find if target-element is in the list
        res = {}
        
        for i in range(len(numbers)):
            x = target - numbers[i]
            if x not in res:
                res[numbers[i]] = i + 1
            else:
                return [res[x], i+1]
        
        
            
                