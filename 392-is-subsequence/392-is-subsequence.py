class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Thinking:
        # for each char in s, if can't find in t, -> False
        # search t for the next char after the position where the previous char is found
        
#         cur_position = 0
#         for char in s:
#             index = t.find(char, cur_position)
            
#             if index == -1:
#                 return False
#             else:
#                 cur_position = index + 1
        
#         return True
        
        # ANOTHER Two pointers solution
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)
        