class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        added = []
        for i in range(n):
            added.append(sum(nums[:i]) + nums[i])
        return added
                