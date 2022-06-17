class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        n = len(nums)
        for num in nums:
            # if num not in dic:
            #     dic[num] = 1
            # else:
            #     dic[num] += 1
            dic[num] = dic.get(num, 0) + 1
            if dic[num] > n//2:
                return num