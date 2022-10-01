class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Sep 30

        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        
        return b
        
        
        
        
        
        
        
        
        
        # No.1 RECURSION. time complexity: O(2^n). Doesn't pass.
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return self.climbStairs(n - 2) + self.climbStairs(n - 1)  
        # ---- That's fibonacci... obviously
        
        # No.2 Top down, memorization. Store the previous result in a dictionary. O(n).
        # dic = {1:1, 2:2}
        # for i in range(3, n+1):
        #     dic[i] = dic[i-1] + dic[i-2]
        # return dic[n]
        
        # No.3 Bottom up Memorization. Dynamic Programing.  Check youtube video
        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one