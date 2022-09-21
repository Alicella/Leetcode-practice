class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Thinking:
        # for each char in s, if can't find in t, -> False
        # search t for the next char after the position where the previous char is found
        
        cur_position = 0
        for char in s:
            index = t.find(char, cur_position)
            
            if index == -1:
                return False
            else:
                cur_position = index + 1
        
        return True