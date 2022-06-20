class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            cur_area = min(height[left], height[right]) * (right - left)
            if cur_area > max_area:
                max_area = cur_area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        
        # max_area = 0
        # for i in range(1,len(height)):
        #     for k in range(i):
        #         cur_area = min(height[k], height[i]) * (i-k)
        #         if cur_area > max_area:
        #             max_area = cur_area
        
    
        return max_area