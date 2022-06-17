class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        
        for num in nums:
            if count == 0:
                res = num
            if num == res:
                count += 1
            else:
                count -= 1
        return res
        
        
        
        
        
        # dic = {}
        # n = len(nums)
        # for num in nums:
        #     dic[num] = dic.get(num, 0) + 1
        #     if dic[num] > n//2:
        #         return num