class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
    
        l, r = 0, 1
        longest = 1
        # window = [s[l]]
        
        while r < len(s):  
#             if s[r] not in window:
#                 window.append(s[r])
#                 longest = max(longest, r - l + 1)
#                 r += 1
            
#             else:
#                 l += 1
#                 window = window[1:]
               
            if s[r] not in s[l:r]:
                longest = max(longest, r - l + 1)
                r += 1
            else:
                l += 1
            
        return longest   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # max_len = 0
        # cur_list = []
        # for char in s:
        #     if char not in cur_list:
        #         cur_list.append(char)
        #         cur_len = len(cur_list)
        #         if cur_len > max_len:
        #             max_len = cur_len
        #     else:
        #         i = cur_list.index(char)
        #         cur_list = cur_list[i+1:] + [char]
        
        max_len = 0
        seen = {}
        l = 0
        
        for r in range(len(s)):
            if s[r] not in seen:
                max_len = max(max_len, r-l+1)
            else:
                if seen[s[r]] < l:
                    max_len = max(max_len, r-l+1)
                else:
                    l = seen[s[r]] + 1
            
            seen[s[r]] = r                        
        
        # left = 0
        # for right, c in enumerate(s):
        #     if c in seen:
        #         left = max(left, seen[c] + 1)
        #     max_len = max(max_len, right - left + 1)
        #     seen[c] = right
        
        
        return max_len
        