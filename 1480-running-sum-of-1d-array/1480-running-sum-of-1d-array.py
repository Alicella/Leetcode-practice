class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cur_sum = 0
        running = []
        for i in range(n):
            cur_sum += nums[i]
            running.append(cur_sum)
        return running
                