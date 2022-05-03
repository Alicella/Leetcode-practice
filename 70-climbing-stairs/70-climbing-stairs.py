class Solution:
    def climbStairs(self, n: int) -> int:
        
        # No.1 RECURSION. time complexity: O(2^n). Doesn't pass.
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return self.climbStairs(n - 2) + self.climbStairs(n - 1)
        
        # No.2 store the previous result in a dictionary
        dic = {1:1, 2:2}
        for i in range(3, n+1):
            dic[i] = dic[i-1] + dic[i-2]
        return dic[n]
        