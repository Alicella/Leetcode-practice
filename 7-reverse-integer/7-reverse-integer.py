class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            sign = -1
        else:
            sign = 1
        
        # recursion method           
#         if abs(x) < 10:
#             return x
        
#         else:
#             x = abs(x)
#             digits = len(str(x))
#             result = (self.reverse(x//10) + (x % 10) * (10 ** (digits - 1))) * sign
        # reverse list
        s = str(abs(x))
        re_s = s[::-1]
        result = int(re_s) * sign    
        
        return result if abs(result) < pow(2, 31) - 1 else 0

        