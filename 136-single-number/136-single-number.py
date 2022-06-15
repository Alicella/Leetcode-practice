class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # loop over the list, create a new list to store numbers met
        # if met a repeated num, delete the num in the list (n/2 space?)
        
#         tmp = []
#         for i in nums:
#             if i not in tmp:
#                 tmp.append(i)
#             else:
#                 tmp.remove(i)
        
#         return tmp[0]
        
        # tmp = {}
#         for i in nums:
#             if i not in tmp:
#                 tmp[i] = 1
#             else:
#                 del tmp[i]
        
#         for k in tmp.keys():
#             return k 
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key, val in dic.items():
            if val == 1:
                return key
         
                